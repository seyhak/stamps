import { AppContainerActionTypes } from 'ACTIONS/AppContainerActions'
import { THEMES } from 'GLOBAL/consts'

function changeTheme(current_theme){
	const currentThemeIndex = THEMES.findIndex((element) => {
		return element==current_theme
	})
	if(currentThemeIndex == THEMES.length - 1){
		return THEMES[0]
	}
	else{
		return THEMES[currentThemeIndex + 1]
	}
}

const initialState = {
	contentPage: 'user',
	theme: 'theme_dark'
}

function appContainerReducer(state = initialState, action) {
	switch(action.type){
	case AppContainerActionTypes.CHANGE_THEME:
		return{
			...state,
			theme: changeTheme(state.theme)
		}
		// otherwise return the existing state unchanged
	default:
		return state
	}
}

export default appContainerReducer
