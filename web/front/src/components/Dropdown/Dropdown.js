import React from 'react'
import PropTypes from 'prop-types'
import { Menu } from 'grommet-icons'
import './Dropdown.sass'
    
function Dropdown(){
	function switchMenu(){
		console.log(123)
	}

	return(
		<div className='Dropdown'>
			<Menu onClick={switchMenu} size='medium'/>
		</div>
	)
}

export default Dropdown