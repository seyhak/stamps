/* eslint-disable indent */
import React from 'react'
import PropTypes from 'prop-types'
import { useDispatch, useSelector } from 'react-redux'

import Card from 'COMPONENTS/Card/Card'
import SearchBar from 'COMPONENTS/SearchBar/SearchBar'
import LoadingSVG from 'COMPONENTS/LoadingSVG/LoadingSVG'
import './UserViewContainer.sass'
import { loadCards } from 'ACTIONS/UserViewContainerActions'

function UserViewContainer(props){
	// const [userViewState, changeUserViewState] = useState(false)
	const { cards, isLoading } = useSelector( state => ({
		cards: state.userViewContainer.cards,
		isLoading: state.userViewContainer.isLoading
	}))
	const dispatch = useDispatch()

	function search(){
		console.log('Search')
	}
	let searchBar = null
	const cardsContent = []
	console.log(cards)
	if(isLoading){
		cardsContent.push(
			<LoadingSVG
				key={0}
				fill='#1e1f21'
			/>
		)
	}
	else if(!isLoading && cards.length == 0){
		dispatch(loadCards())
	}
	else{
		searchBar = (<SearchBar
			searchFunction={search}
			size='large'
			theme={props.theme}
		/>)
		//static cards
		for (let i = 0; i < 2; i++) {
			const cardInfo = {
				'amountFilled': 2,
				'amountTotal': 7,
				'companyName': 'AbComp',
				'companyLogo': 'https://interactive-examples.mdn.mozilla.net/media/examples/grapefruit-slice-332-332.jpg',
				'companyStampLogo': 'http://www.pngall.com/wp-content/uploads/2016/07/Sun-Download-PNG.png',
				'companyBackground': null, 
			}
			cardsContent.push(
				<Card
					key={i}
					cardInfo={cardInfo}
					theme={props.theme}
				/>
			)
		}
	}

	return(
		<div className={'UserViewContainer ' + props.theme}>
            {searchBar}
			<div className='cards_container'>
				{cardsContent}
			</div>
		</div>
	)
}

UserViewContainer.propTypes = {
	theme: PropTypes.string
}

export default UserViewContainer
