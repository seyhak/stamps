import React from 'react'

import { render, fireEvent } from '@testing-library/react'
import { Provider } from "react-redux"

import { Dropdown } from 'COMPONENTS/Dropdown/Dropdown'
import DropdownOption from 'GLOBAL/classes/DropdownOption'
import store from 'GLOBAL/store'

describe('Dropdown', () => {
	const options = [
		new DropdownOption('login'),
		new DropdownOption('12')
	]
	const myMock = jest.fn()
	const theme = 'theme_dark'

	test('dropdown icon and menu', () => {
		const dropdown = render(
			<Provider store={store}>
				<Dropdown
					changeTheme={myMock}
					options={options}
					theme={theme}
				/>
			</Provider>
		)
		// render icon
		expect(dropdown.baseElement.getElementsByClassName('dropdown')).toBeDefined()
		expect(document.querySelector('button')).toBeNull()
		// open menu
		fireEvent.click(dropdown.baseElement.getElementsByClassName('dropdown')[0])
		expect(dropdown.baseElement.getElementsByClassName('dropdown_menu_option')).toHaveLength(2)
		// check if theme switcher was rendered
		expect(dropdown.baseElement.getElementsByClassName('theme_switcher')).toBeDefined()
		// check rendered options
		expect(dropdown.baseElement.querySelectorAll('.dropdown_menu_option')).toHaveLength(options.length)
		fireEvent.click(dropdown.baseElement.getElementsByClassName('theme_switcher')[0])
		// expect theme to be changed
		expect(myMock.mock.calls).toHaveLength(1)
		// check if closing works fine
		fireEvent.click(dropdown.baseElement.getElementsByClassName('dropdown')[0])
		expect(dropdown.baseElement.querySelector('.theme_switcher')).toBeNull()
		// reopen and check if closing by clicking on dropdown_menu_container works
		fireEvent.click(dropdown.baseElement.getElementsByClassName('dropdown')[0])
		fireEvent.click(dropdown.baseElement.getElementsByClassName('dropdown_menu_container')[0])
		expect(dropdown.baseElement.querySelector('.theme_switcher')).toBeNull()

	})
})
