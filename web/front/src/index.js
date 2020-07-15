import React from 'react'
import ReactDOM from 'react-dom'
import AppContainer from  './containers/AppContainer/AppContainer'
import { Provider } from "react-redux"

import store from 'GLOBAL/store'
    
class App extends React.Component{
	render(){
		return(
			<Provider store={store}>
				<AppContainer/>
			</Provider>
		)
	}
}

ReactDOM.render(
	<App/>,
	document.getElementById('root')
)

export default App