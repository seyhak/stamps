import React from 'react'
import PropTypes from 'prop-types'
import './Navbar.sass'

import DropdownOption from '../../global/classes/DropdownOption'
import { Dropdown } from '../Dropdown/Dropdown'

function Navbar(props){
	const options = [
		new DropdownOption('login'),
		new DropdownOption('chuj'),
		new DropdownOption('Change Theme')
	]
	return(
		<div className={'navbar secondary ' + props.theme}>
			<div className={'title secondary ' + props.theme}>Stamps</div>
			<Dropdown
				changeTheme={props.changeTheme}
				options={options}
				theme={props.theme}
			/>
		</div>
	)
}

Navbar.propTypes = {
	changeTheme: PropTypes.func,
	theme: PropTypes.string
}
export default Navbar