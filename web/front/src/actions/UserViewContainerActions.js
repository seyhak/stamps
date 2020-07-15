import { createAction } from '@reduxjs/toolkit'

export const UserViewContainerActionTypes = {
	FAILURE: 'userViewContainerActionTypes/failure',
	REQUEST: 'userViewContainerActionTypes/request',
	SUCCESS: 'userViewContainerActionTypes/success'
}

function requestCards(){
	return{
		type: UserViewContainerActionTypes.REQUEST
	}
}
function requestCardsSuccess(json){
	return {
		json: json,
		type: UserViewContainerActionTypes.SUCCESS
	}
}

export const requestCardsFailure = createAction(
	UserViewContainerActionTypes.FAILURE
)

export function loadCards (){
	return  dispatch => {
		dispatch(requestCards())
		return fetch(`https://www.instagram.com/seyhakly1/?__a=1`)
			.then(response => response.json())
			.then(json =>dispatch(requestCardsSuccess(json))
			)
	}
}
