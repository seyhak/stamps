import URI from 'urijs'
import fetch from 'node-fetch'

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
function requestCardsSuccess(jsonData){
	return {
		json: jsonData,
		type: UserViewContainerActionTypes.SUCCESS
	}
}

export const requestCardsFailure = createAction(
	UserViewContainerActionTypes.FAILURE
)

export function loadCards (){
	return  dispatch => {
		dispatch(requestCards())
		
		const uri = new URI('http://127.0.0.1:8000/api/get_my_cards/')
		const url = uri.toString()

		return fetch(url, {
			method: 'GET',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json'
			},
		})
			.then(
				response => response.json()
			)
			.then(json => dispatch(requestCardsSuccess(json)))
	}
}
