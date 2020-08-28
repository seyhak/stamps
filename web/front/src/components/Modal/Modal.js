import React from 'react'
import PropTypes from 'prop-types'
import './Modal.sass'

function ModalButton(props){
	return(
		<button className='button' onClick={props.onClick}>
			{props.text}
		</button>
	)
}

function Modal(props){
	const buttons = props.modalButtons.map(button => {
		<ModalButton
			onClick={button.onClick}
			text={button.text}
		/>
	})

	return(
		<div className={'modal ' + props.theme}>
			<div className="modal_content">
				<span className="close"></span>
				<p>{props.modalText}</p>
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