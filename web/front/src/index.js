import React from 'react'
import ReactDOM from 'react-dom'
import AppContainer from  './containers/AppContainer/AppContainer'
// import  './main.css'
    
class App extends React.Component{
	render(){
		return(
			<AppContainer/>
		)
	}
}

ReactDOM.render(
	<App/>,
	document.getElementById('root')
)

export default App