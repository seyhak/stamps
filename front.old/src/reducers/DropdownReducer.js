import { DropdownActionTypes } from 'ACTIONS/DropdownActions'

const initialState = {
	menuOpened: false
}

function dropdownReducer(state = initialState, action) {
	switch(action.type){
	case DropdownActionTypes.SWITCH_DROPDOWN:
		return{
			...state,
			menuOpened: !state.menuOpened
		}
	default:
		return state
	}
}

export default dropdownReducer
