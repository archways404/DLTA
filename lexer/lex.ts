// Define token types
enum TokenType {
	CommentSingleLine,
	VariableDeclaration,
	// Add other token types as needed
}

// Define the token structure
interface Token {
	tokenType: TokenType;
	lexeme: string;
}

// Tokenize function
function tokenize(input: string): Token[] {
	const tokens: Token[] = [];
	const lines = input.split('\n');

	for (const line of lines) {
		const trimmedLine = line.trim();

		// Handle single line comments
		if (trimmedLine.startsWith('COMMENT:')) {
			tokens.push({
				tokenType: TokenType.CommentSingleLine,
				lexeme: trimmedLine.substring('COMMENT:'.length).trim(),
			});
		}
		// Handle variable declarations
		else if (trimmedLine.startsWith('VARIABLE:')) {
			tokens.push({
				tokenType: TokenType.VariableDeclaration,
				lexeme: trimmedLine.substring('VARIABLE:'.length).trim(),
			});
		}
		// Add other tokenization rules as needed
	}

	return tokens;
}

// Example usage
const input1 = `
  COMMENT: This is a single line comment
  VARIABLE: VAR(M, STRING) = 'HELLO WORLD'
`;

const tokens = tokenize(input1);
console.log(tokens);
