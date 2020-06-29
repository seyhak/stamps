import React from 'react'
import PropTypes from 'prop-types'
import './Navbar.sass'

import Dropdown from '../Dropdown/Dropdown'
    
function Navbar(){
	return(
		<div className="Navbar">
			<div>Stamps</div>
			<Dropdown></Dropdown>
		</div>
	)
}

export default Navbar