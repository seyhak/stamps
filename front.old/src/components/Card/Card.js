import React, { useState } from 'react'
import PropTypes, { string } from 'prop-types'

import './Card.sass'

function CardStamp(props){
	return(
		<div className='card_stamp'>
			<img className='card_stamp_company_logo_image' src={props.companyStampLogo}/>
			<img className='card_stamp_company_background_image' src={props.backgroundImageSource}/>
		</div>
	)
}

CardStamp.propTypes = {
	companyStampLogo: PropTypes.string,
	backgroundImageSource: PropTypes.string,
	filled: PropTypes.bool,
	height: PropTypes.number,
	theme: PropTypes.string
}

function Card(props){
	function getStampPerRow(rowsAmount, stampsAmount){
		return Math.ceil(stampsAmount / rowsAmount)
	}

	const rows = []
	const maxStampsPerRow = 5
	const rowsAmount = Math.ceil(props.cardInfo['maximumStamps'] / maxStampsPerRow)
	const height = (100 / rowsAmount).toString() + '%'

	let addedStamps = 0
	const stampsPerRow = getStampPerRow(rowsAmount, props.cardInfo['maximumStamps'])
	//rows
	for (let rowIndex = 0; rowIndex < rowsAmount; rowIndex++){
		let stamps = []
		//stamps per row
		for (let index = 0; index < stampsPerRow; index++){
			if (addedStamps == props.cardInfo['maximumStamps']){
				break
			}
			stamps.push(
				<CardStamp
					key={addedStamps}
					companyStampLogo={props.cardInfo['companyLogo']}
					backgroundImageSource={props.cardInfo['companyStampLogo']}
					theme={props.theme}
				/>
			)
			addedStamps++
		}
		rows.push(
			<div key={rowIndex} className='card_stamps_row' style={{height: height}}>
				{stamps}
			</div>
		
		)
	}

	return(
		<div className={'Card secondary ' + props.theme}>
			<div className='card_header'>
				<img className='logo' src={props.cardInfo['companyLogo']}/>
				<div className='title'>{props.cardInfo['companyName']}</div>
			</div>
			
			<div className='card_stamps_container'>
				{rows}
			</div>
		</div>
	)
}

Card.propTypes = {
	cardInfo: PropTypes.object,
	theme: PropTypes.string
}


export default Card
