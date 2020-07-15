import { UserViewContainerActionTypes } from 'ACTIONS/UserViewContainerActions'

const initialState = {
	cards: [],
	isLoading: false
}

function userViewContainerReducer(state = initialState, action) {
	// Check to see if the reducer cares about this action
	switch(action.type){
	case UserViewContainerActionTypes.REQUEST:
		return{
			...state,
			isLoading: true
		}
	case UserViewContainerActionTypes.SUCCESS:
		return{
			...state,
			cards: [123],
			isLoading: false
		}
	case UserViewContainerActionTypes.FAILURE:
		return{
			...state,
			isLoading: false
		}
	default:
		return state
	}
}

export default userViewContainerReducer
