import React from 'react'

import { render, fireEvent } from '@testing-library/react'
import { screen } from '@testing-library/dom'
import { Provider } from "react-redux"

import UserViewContainer from 'CONTAINERS/UserViewContainer/UserViewContainer'
import LoadingSVG from 'COMPONENTS/LoadingSVG/LoadingSVG'

import store from 'GLOBAL/store'

describe('UserViewContainer', () => {
	jest.mock('COMPONENTS/LoadingSVG/LoadingSVG')
	const LoadingSVGMock = jest.doMock()
	const theme = 'theme_dark'

	afterEach(() => {
	})

	test('UserViewContainer renders loading SVG', () => {
		// mock fetch
		global.fetch = jest.fn(() =>
			Promise.resolve({
				json: () => Promise.resolve({}),
			})
		)
		render(
			<Provider store={store}>
				<UserViewContainer
					theme={theme}
				/>
			</Provider>
		)

		expect(document.querySelector('.UserViewContainer').className).toBe('UserViewContainer theme_dark')
		expect(document.querySelector('.loading_svg')).toBeInstanceOf(SVGSVGElement)
	})

	test.skip('UserViewContainer renders cards', () => {
		// mock fetch
		const cards = {
			'amountFilled': 2,
			'amountTotal': 7,
			'companyName': 'AbComp',
			'companyLogo': 'https://interactive-examples.mdn.mozilla.net/media/examples/grapefruit-slice-332-332.jpg',
			'companyStampLogo': 'http://www.pngall.com/wp-content/uploads/2016/07/Sun-Download-PNG.png',
			'companyBackground': null, 
		}
		global.fetch = jest.fn(() =>
			Promise.resolve({
				json: () => Promise.resolve({}),
			})
		)
		const component = render(
			<Provider store={store}>
				<UserViewContainer
					theme={theme}
				/>
			</Provider>
		)
		console.log(document.getElementsByClassName('Card'))
		expect(document.getElementsByClassName('Card'))
		expect(document.querySelector('.UserViewContainer').className).toBe('UserViewContainer theme_dark')
		expect(document.querySelector('.loading_svg')).toBeInstanceOf(SVGSVGElement)
	})
})
