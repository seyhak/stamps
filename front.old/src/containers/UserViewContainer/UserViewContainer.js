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

		for (let i = 0; i < cards.length; i++) {
			const cardInfo = {
				'collectedStamps': cards[i].collected_stamps,
				'maximumStamps': cards[i].maximum_stamps,
				'companyName':  cards[i].company_name,
				'companyLogo': cards[i].company_logo_url,
				'companyStampLogo': cards[i].company_stamp_url,
				'companyBackground': cards[i].company_background_image_url, 
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
