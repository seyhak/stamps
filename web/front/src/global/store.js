import { configureStore } from '@reduxjs/toolkit'

import userViewContainerReducer from 'REDUCERS/UserViewContainerReducer'
import appContainerReducer from 'REDUCERS/AppContainerReducer'
import dropdownReducer from 'REDUCERS/DropdownReducer'

const store = configureStore({
	reducer: {
		appContainer: appContainerReducer,
		dropdown: dropdownReducer,
		userViewContainer: userViewContainerReducer
	}
})

export default store
