module.exports = {
	'moduleNameMapper': {
		'^COMPONENTS(.*)$': '<rootDir>/src/components$1',
		'^GLOBAL(.*)$': '<rootDir>/src/global$1',
		'^.+\\.(css|sass|scss)$': 'babel-jest'
	},
	verbose: true,
}
