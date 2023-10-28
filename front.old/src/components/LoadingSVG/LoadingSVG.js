import React from 'react'
import PropTypes from 'prop-types'

import './LoadingSVG.sass'

function LoadingSVG(props){
	return (
		<svg className='loading_svg' width="200px" height="200px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
			<g transform="rotate(0 50 50)">
				<rect x="48" y="21" rx="2" ry="4.8" width="4" height="12" fill={props.fill}>
					<animate attributeName="opacity" values="1;0" keyTimes="0;1" dur="1.020408163265306s" begin="-0.8746355685131195s" repeatCount="indefinite"></animate>
				</rect>
			</g><g transform="rotate(51.42857142857143 50 50)">
				<rect x="48" y="21" rx="2" ry="4.8" width="4" height="12" fill={props.fill}>
					<animate attributeName="opacity" values="1;0" keyTimes="0;1" dur="1.020408163265306s" begin="-0.7288629737609329s" repeatCount="indefinite"></animate>
				</rect>
			</g><g transform="rotate(102.85714285714286 50 50)">
				<rect x="48" y="21" rx="2" ry="4.8" width="4" height="12" fill={props.fill}>
					<animate attributeName="opacity" values="1;0" keyTimes="0;1" dur="1.020408163265306s" begin="-0.5830903790087463s" repeatCount="indefinite"></animate>
				</rect>
			</g><g transform="rotate(154.28571428571428 50 50)">
				<rect x="48" y="21" rx="2" ry="4.8" width="4" height="12" fill={props.fill}>
					<animate attributeName="opacity" values="1;0" keyTimes="0;1" dur="1.020408163265306s" begin="-0.43731778425655976s" repeatCount="indefinite"></animate>
				</rect>
			</g><g transform="rotate(205.71428571428572 50 50)">
				<rect x="48" y="21" rx="2" ry="4.8" width="4" height="12" fill={props.fill}>
					<animate attributeName="opacity" values="1;0" keyTimes="0;1" dur="1.020408163265306s" begin="-0.29154518950437314s" repeatCount="indefinite"></animate>
				</rect>
			</g><g transform="rotate(257.14285714285717 50 50)">
				<rect x="48" y="21" rx="2" ry="4.8" width="4" height="12" fill={props.fill}>
					<animate attributeName="opacity" values="1;0" keyTimes="0;1" dur="1.020408163265306s" begin="-0.14577259475218657s" repeatCount="indefinite"></animate>
				</rect>
			</g><g transform="rotate(308.57142857142856 50 50)">
				<rect x="48" y="21" rx="2" ry="4.8" width="4" height="12" fill={props.fill}>
					<animate attributeName="opacity" values="1;0" keyTimes="0;1" dur="1.020408163265306s" begin="0s" repeatCount="indefinite"></animate>
				</rect>
			</g>
		</svg>
	)
}

LoadingSVG.propTypes = {
	fill: PropTypes.string
}

export default LoadingSVG
