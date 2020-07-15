module.exports = {
	'moduleNameMapper': {
		'^ACTIONS(.*)$': '<rootDir>/src/actions$1',
		'^COMPONENTS(.*)$': '<rootDir>/src/components$1',
		'^CONTAINERS(.*)$': '<rootDir>/src/containers$1',
		'^REDUCERS(.*)$': '<rootDir>/src/reducers$1',
		'^GLOBAL(.*)$': '<rootDir>/src/global$1',
		'^.+\\.(css|sass|scss)$': 'babel-jest'
	},
	verbose: true,
}
