import React from 'react'
import PropTypes from 'prop-types'
import './AppContainer.sass'

import Footer from '../../components/Footer/Footer'
import Navbar from '../../components/Navbar/Navbar'

function AppContainer(){
	return(
		<div className='AppContainer dark'>
			<Navbar/>

			<Footer>

			</Footer>
		</div>
	)
}

export default AppContainer