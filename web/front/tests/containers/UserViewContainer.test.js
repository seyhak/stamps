import React from 'react'

import { render, waitFor } from '@testing-library/react'
import { Provider } from "react-redux"
import fetch from 'node-fetch'
jest.mock('node-fetch')

import UserViewContainer from 'CONTAINERS/UserViewContainer/UserViewContainer'
import store from 'GLOBAL/store'

describe('UserViewContainer', () => {
	const theme = 'theme_dark'

	// probably store is not being cleansed - leaks to the other test
	test.skip('UserViewContainer renders loading SVG', () => {
		// mock fetch
		fetch.mockImplementation(() => Promise.resolve({
			json: () => Promise.resolve({})
		}))

		const {unmount} = render(
			<Provider store={store}>
				<UserViewContainer
					theme={theme}
				/>
			</Provider>
		)
		
		expect(document.querySelector('.UserViewContainer').className).toBe('UserViewContainer theme_dark')
		expect(document.querySelector('.loading_svg')).toBeInstanceOf(SVGSVGElement)
	})

	test('UserViewContainer renders cards', async () => {
		const cards = [{
			'collected_stamps': 2,
			'maximum_stamps': 7,
			'company_name': 'AbComp',
			'company_logo_url': 'https://interactive-examples.mdn.mozilla.net/media/examples/grapefruit-slice-332-332.jpg',
			'company_stamp_url': 'http://www.pngall.com/wp-content/uploads/2016/07/Sun-Download-PNG.png',
			'company_background_image_url': null, 
		}]
		// mock fetch
		fetch.mockImplementation(() => Promise.resolve({
			json: () => Promise.resolve(cards)
		}))
		const component = render(
			<Provider store={store}>
				<UserViewContainer
					theme={theme}
				/>
			</Provider>
		)
		expect(document.querySelector('.UserViewContainer').className).toBe('UserViewContainer theme_dark')
		await waitFor(() => {
			expect(document.querySelector('.Card')).toBeDefined()
			expect(document.querySelector('.card_stamp_company_background_image').src).toEqual(
				cards[0].company_stamp_url
			)
			expect(document.querySelector('.card_stamp_company_logo_image').src).toEqual(
				cards[0].company_logo_url
			)
			expect(document.getElementsByClassName('card_stamp').length).toEqual(
				cards[0].maximum_stamps
			)
		})
	})
})
