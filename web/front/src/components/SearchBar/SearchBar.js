import React, { useState } from 'react'
import PropTypes from 'prop-types'
import { Search } from 'grommet-icons'

import './SearchBar.sass'

function SearchBar(props){
	return(
		<div className={'SearchBar input ' + props.theme}>
			<input type="text" id="fname" name="fname"></input>
			
			<Search
				className='search input'
				color='black'
				onClick={props.searchFunction}
				size='large'
			/>
		</div>
	)
}

SearchBar.propTypes = {
	searchFunction: PropTypes.func,
	theme: PropTypes.string
}

export default SearchBar
