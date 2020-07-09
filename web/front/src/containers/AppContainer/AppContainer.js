import React, { useState } from 'react'
import PropTypes from 'prop-types'
import './AppContainer.sass'

import { THEMES } from '../../global/consts'
import { DropdownMenu } from '../../components/Dropdown/Dropdown'
import Footer from '../../components/Footer/Footer'
import Navbar from '../../components/Navbar/Navbar'

function AppContainer(){
	const [content, setContent] = useState(null)
	const [theme, setTheme] = useState('theme_dark')
	let className = 'AppContainer' + ' ' + theme

	function changeTheme(){
		const currentThemeIndex = THEMES.findIndex((element) => {
			return element==theme
		})
		if(currentThemeIndex == THEMES.length - 1){
			setTheme(THEMES[0])
		}
		else{
			setTheme(THEMES[currentThemeIndex + 1])
		}
	}

	return(
		<div className={className}>
			<Navbar changeTheme={changeTheme} theme={theme}/>
			<div className='body'>
				{content}
			</div>
			{/* <Footer/> */}
		</div>
	)
}

export default AppContainer