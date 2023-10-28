import React, { useState } from 'react'
import PropTypes from 'prop-types'
import './AppContainer.sass'
import { useDispatch, useSelector } from 'react-redux'

import { THEMES } from 'GLOBAL/consts'
import { changeTheme } from 'ACTIONS/AppContainerActions'
import { DropdownMenu } from 'COMPONENTS/Dropdown/Dropdown'
import UserViewContainer from 'CONTAINERS/UserViewContainer/UserViewContainer'
import Footer from 'COMPONENTS/Footer/Footer'
import Navbar from 'COMPONENTS/Navbar/Navbar'


function AppContainer(){
	const { contentPage, theme } = useSelector(state => ({
		contentPage: state.appContainer.contentPage,
		theme: state.appContainer.theme
	}))
	const dispatch = useDispatch()

	let content = null
	let className = 'AppContainer' + ' ' + theme

	switch(contentPage){
	case 'home':
		break
	case 'user':
		content = (
			<UserViewContainer
				theme={theme}
			/>
		)
		break
	}

	return(
		<div className={className}>
			<Navbar changeTheme={() => dispatch(changeTheme())} theme={theme}/>
			<div className='body'>
				{content}
			</div>
			{/* <Footer/> */}
		</div>
	)
}

export default AppContainer