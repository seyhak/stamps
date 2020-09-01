import React from 'react'
import PropTypes from 'prop-types'
import './Modal.sass'

function ModalButton(props){
	return(
		<button className='modal_button' onClick={props.onClick}>
			{props.text}
		</button>
	)
}

function Modal(props){
	const buttons = props.modalButtons.map((button, index) => {
		return(
			<ModalButton
				key={index}
				onClick={button.onClick}
				text={button.text}
			/>
		)
	})
	console.log(buttons)
	return(
		<div className={'Modal secondary ' + props.theme}>
			<div className='modal_content'>
				{/* <span className="close"></span> */}
				<div className='modal_header'>{props.header}</div>
				<div className='modal_body'>{props.modalText}</div>
			</div>
			<div className='modal_footer'>
				{buttons}
			</div>
		</div>
	)
}

Modal.defaultProps = {
	header: 'Header',
	modalText: 'Header',
	modalButtons: [],
	theme: ''
}

Modal.propTypes = {
	header: PropTypes.string,
	modalText: PropTypes.string,
	modalButtons: PropTypes.array,
	theme: PropTypes.string
}

ModalButton.propTypes = {
	onClick: PropTypes.func,
	text: PropTypes.string
}

export default Modal