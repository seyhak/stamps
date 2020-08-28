import React, { useState } from 'react'
import './AppContainer.sass'
import { useDispatch, useSelector } from 'react-redux'

import { THEMES } from 'GLOBAL/consts'
import { changeTheme } from 'ACTIONS/AppContainerActions'
import DropdownOption from 'GLOBAL/classes/DropdownOption'
import Modal from 'COMPONENTS/Modal/Modal'
import UserViewContainer from 'CONTAINERS/UserViewContainer/UserViewContainer'
import Footer from 'COMPONENTS/Footer/Footer'
import Navbar from 'COMPONENTS/Navbar/Navbar'


function AppContainer(){
	const { contentPage, theme } = useSelector(state => ({
		contentPage: state.appContainer.contentPage,
		theme: state.appContainer.theme
	}))
	const [modal, setModal] = useState(null)
	const dispatch = useDispatch()

	let content = null
	let className = 'AppContainer' + ' ' + theme
	let navbarOptions = null
	// let modal = null

	function LoginOrRegister(){
		console.log(123123)
		setModal(
			<Modal 

			/>
		)
		console.log(modal)
			
	}

	switch(contentPage){
	case 'undefined':
		navbarOptions = [
			new DropdownOption('Login or Register', null, LoginOrRegister)
		]
		break
	case 'user':
		content = (
			<UserViewContainer
				theme={theme}
			/>
		)
		navbarOptions = [
			new DropdownOption('User stuff', null, LoginOrRegister),
			new DropdownOption('Logout', null, LoginOrRegister)
		]
		break
	case 'business':
		content = (
			<UserViewContainer
				theme={theme}
			/>
		)
		navbarOptions = [
			new DropdownOption('Business stuff', null, LoginOrRegister),
			new DropdownOption('Logout', null, LoginOrRegister)
		]
		break
	}

	return(
		<div className={className}>
			<Navbar 
				changeTheme={() => dispatch(changeTheme())}
				options={navbarOptions}
				theme={theme}
			/>
			<div className='body'>
				{modal}
				{content}
			</div>
			{/* <Footer/> */}
		</div>
	)
}

export default AppContainer