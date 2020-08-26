import React from 'react'
import PropTypes from 'prop-types'
import './Navbar.sass'

import { Dropdown } from '../Dropdown/Dropdown'

function Navbar(props){
	const options = props.options
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
	options: PropTypes.array,
	theme: PropTypes.string
}
export default Navbar