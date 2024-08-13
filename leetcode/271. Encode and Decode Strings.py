# use a delimiter '/:' and a escape '/' char
# if the original string already have '/', add a '/'
# if the original string already have '/:' => '//:/:'

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        encoded = ''
        for str in strs:
            encoded += str.replace('/', '//') + '/:'

        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        decoded = []

        current_string = ''
        i = 0 

        while i < len(s):
            if s[i:i+2] == '/:':
                decoded.append(current_string)
                current_string = ''
                i += 2
            elif s[i:i+2] == '//':
                current_string += '/'
                i += 2
            else:
                current_string += s[i]
                i += 1
        
        return decoded


# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = ["Hello", "World/:", "How/are you?"]
encoded = codec.encode(strs)
print(encoded) 
# Hello/:World//:/:How//are you?/:
print(codec.decode(encoded))