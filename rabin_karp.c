#include <stdio.h>
#include <string.h>
const unsigned BASE = 257;
const unsigned MOD = 1000000007;


int hash(const char* input)
{
	long long digest = 0;
	for (int i = 0; i < strlen(input);i++)
	{
		// calculates hash using rolling hash function.
		digest = digest * BASE + input[i]; 
		digest = digest % MOD;
	}
	return digest;

}

int rabin_karp(char* text, char* pattern)
{
	long long hash_pattern = hash(pattern);
	long long hash_text = 0;
	long long exponent = 1;
	for (int i = 0; i < strlen(pattern);i++)
	{
		exponent = (exponent * BASE) % MOD;

		for(int i = 0; i < strlen(text);i++)
		{
			hash_text = hash_text * BASE + text[i];
			hash_text = hash_text % MOD;

			if( i >= strlen(pattern))
			{
				hash_text -= exponent * text[i - strlen(pattern)] % MOD;
				if(hash_text < 0)
				{
					hash_text = hash_text + MOD;
				}
			}
			if( i >= strlen(pattern) - 1)
			{
				if( hash_text == hash_pattern)
				{
					 return i - (strlen(pattern)-1);
				}
			}
		}

	}	
}

int main()
{
	printf("%d",rabin_karp("chicken","k"));
	return 0;
}




