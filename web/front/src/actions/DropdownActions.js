import { createAction } from '@reduxjs/toolkit'

export const DropdownActionTypes = {
	SWITCH_DROPDOWN: 'dropdownActionTypes/switch_dropdown'
}

const switchDropdown = createAction(DropdownActionTypes.SWITCH_DROPDOWN)

export { switchDropdown }