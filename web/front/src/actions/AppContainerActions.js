import { createAction } from '@reduxjs/toolkit'

export const AppContainerActionTypes = {
	CHANGE_THEME: 'appContainerActionTypes/change_theme',
	LOAD_INITIAL_DATA: 'appContainerActionTypes/load_initial_data'
}

export const changeTheme = createAction(AppContainerActionTypes.CHANGE_THEME)
export const loadInitialData = createAction(AppContainerActionTypes.LOAD_INITIAL_DATA)
