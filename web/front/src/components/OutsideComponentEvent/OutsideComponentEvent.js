import React from 'react'
import PropTypes from 'prop-types'
import './OutsideComponentEvent.sass'



function OutsideComponentEvent(props){
	return(
		<div className='OutsideComponentEvent' onClick={props.onClick}></div>
	)
}

OutsideComponentEvent.propTypes = {
	onClick: PropTypes.func
}
export default OutsideComponentEvent