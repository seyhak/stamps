import React, { useState }  from 'react'
import PropTypes from 'prop-types'
import { Menu, StatusUnknownSmall } from 'grommet-icons'
import './Dropdown.sass'


function Dropdown(props){
	const [menuState, switchMenu] = useState(false)
	let dropdownMenu = null

	function onMenuClick(){
		switchMenu(!menuState)
	}
	if(menuState){
		dropdownMenu = (
			<DropdownMenu
				changeTheme={props.changeTheme}
				switchMenu={switchMenu}
				theme={props.theme}
				options={props.options}
			/>
		)
	}
	return(
		<div className='dropdown_container'>
			<Menu 
				className='dropdown'
				onClick={onMenuClick}
				size='large'
			/>
			{dropdownMenu}
		</div>
	)
}

function DropdownMenu(props){
	let listOfOptions = []
	props.options.forEach((element, index) => {
		listOfOptions.push(
			<button
				key={index}
				className={
					'dropdown_menu_option clickable secondary '
					+ element.class
					+ ' ' + props.theme
				}
				onClick={element.onClick}
			>{element.text}</button>
		)
	})
	
	function switchDropdownMenu(element){
		if(element.target.localName == 'div'){
			props.switchMenu(false)
		}
	}

	return(
		<div className='dropdown_menu_container' onClick={(element)=>switchDropdownMenu(element)}>
			<div className={'dropdown_menu third ' + props.theme}>
				{listOfOptions}
				<StatusUnknownSmall
					className='theme_switcher'
					onClick={props.changeTheme}
					size='xlarge'
				/>
			</div>
		</div>
	)
}

Dropdown.propTypes = {
	changeTheme: PropTypes.func,
	options: PropTypes.array,
	theme: PropTypes.string
}

DropdownMenu.propTypes = {
	changeTheme: PropTypes.func,
	options: PropTypes.array,
	switchMenu: PropTypes.func,
	theme: PropTypes.string
}
export {Dropdown, DropdownMenu}
