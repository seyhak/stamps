import React, { useState } from 'react'
import './AppContainer.sass'
import { useDispatch, useSelector } from 'react-redux'

import { THEMES } from 'GLOBAL/consts'
import { changeTheme } from 'ACTIONS/AppContainerActions'
import { switchDropdown } from 'ACTIONS/DropdownActions'
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
	const [loginRegisterModalOpened, setLoginRegisterModal] = useState(false)
	const dispatch = useDispatch()

	let content = null
	let className = 'AppContainer' + ' ' + theme
	let navbarOptions = null
	// let modal = null

	function Login(){
		console.log('Logir')
	}

	function Register(){
		console.log('Register')
	}

	function SwitchLoginOrRegisterModal(){
		if(!loginRegisterModalOpened){
			dispatch(switchDropdown())
		}
		setLoginRegisterModal(!loginRegisterModalOpened)
	}

	switch(contentPage){
	case 'undefined':
		navbarOptions = [
			new DropdownOption('Login or Register', null, SwitchLoginOrRegisterModal)
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
				{
					loginRegisterModalOpened ? (
						<Modal 
							modalButtons={[
								{'onClick': Login, 'text': 'Login'},
								{'onClick': Register, 'text': 'Register'}
							]}
							header='Login or Register'
							outsideModalClick={SwitchLoginOrRegisterModal}
							theme={theme}
						/>
					) : null
				}
				{content}
			</div>
			{/* <Footer/> */}
		</div>
	)
}

export default AppContainer