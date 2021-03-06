import aiohttp
import urllib.parse
import asyncio

def br_invalid(br):
    try:
        if br >= 0 and br <= 255:
            return False
        else:
            return True
    except:
        return True

# --------------------
# |     Classes      |
# --------------------

class Client:
    '''An object that represents the client.

    An object that represents the client to connect to
    the API. With the Client object you can request any
    of the API's endpoints.
    '''

    def __init__(self, token, dev=False):
        '''Constructs the Client.

        Constructs the Client to be used for requests.
        Arguments listed below.

        token (str): This is your API key that you should have
        received from the API website.

        dev (bool): Whether to use the development API
        version or not. Defaults to False.

        session (aiohttp.ClientSession): You can pass a ClientSession
        for the Client to use, if not, the Client will create its own
        session. Defaults to aiohttp.ClientSession.
        '''

        self.token = token
        self.dev = dev
        self.session = aiohttp.ClientSession(loop=asyncio.get_event_loop()) # Fixed the UserInputError.
        self.headers = {
          "Authorization" if self.dev else "token": self.token
        }
        self.base_url = "https://dev.anidiots.guide" if self.dev else "https://api.anidiots.guide"

    def __repr__(self):
        '''Return a eval-safe string representation of the object.'''

        return "<IdioticAPI Client>"

    def __str__(self):
        '''Return a string representation of the object.'''

        return "<IdioticAPI Client, dev={}, url={}>".format(self.dev, self.base_url)

    async def _get(self, endpoint, query):
        '''Request the actual return from the API.

        Request the actual return from the API. Should
        never be called directly.
        '''

        async with self.session.get("{}{}{}".format(self.base_url, endpoint, query.replace('webp', 'png')), headers=self.headers) as resp:
            if resp.status != 200:
                raise Exception("API Returned a non 200 code: {}".format(resp.status))
            data = await resp.json()
        return bytes(data["data"])

    async def _text(self, endpoint, text, style=None):
        """Helper function for text endpoints."""
        params = { "text": text }
        if style: params["style"] = style
        async with self.session.get("{}/text/{}".format(self.base_url, endpoint), headers=self.headers, params=params) as resp:
            # TODO, use params for all querystrings instead?
            if resp.status != 200:
                raise Exception("API Returned a non 200 code: {}".format(resp.status))
            data = await resp.json()
            return data["text"]

    async def blame(self, name):
        '''Returns a blame image in byte form.

        Returns a blame image in byte form. Write
        it to an image file.

        Params:

        name (str): Name to be displayed in the image.
        '''

        return await self._get("/generators/blame" if self.dev else "/blame", "?name={}".format(name))

    async def triggered(self, avatar):
        '''Returns a triggered image in byte form.

        Returns a triggered image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to image to be filtered.
        '''

        return await self._get("/generators/triggered" if self.dev else "/triggered", "?avatar={}".format(avatar))

    async def wanted(self, avatar):
        '''Returns a wanted image in byte form.

        Returns a wanted image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to image to be filtered.
        '''

        return await self._get("/generators/wanted" if self.dev else "/wanted", "?avatar={}".format(avatar))

    async def missing(self, avatar, text):
        '''Returns a missing image in byte form.

        Returns a missing image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to image to be filtered.
        text (str): Text to be written on the image.
        '''

        if not self.dev:
            raise NotAvailable("Missing endpoint is disabled while in production")
        return await self._get("/generators/missing", "?avatar={}&text={}".format(avatar, text))

    async def pls(self, name):
        '''Returns a pls image in byte form.

        Returns a pls image in byte form. Write
        it to an image file.

        Params:

        name (str): Text to be written on the image.
        '''

        return await self._get("/generators/pls" if self.dev else "/pls", "?name={}".format(name))

    async def snapchat(self, text):
        '''Returns a snapchat image in byte form.

        Returns a snapchat image in byte form. Write
        it to an image file.

        Params:

        text (str): Text to be written on the image.
        '''

        return await self._get("/generators/snapchat" if self.dev else "/snapchat", "?text={}".format(text))

    async def achievement(self, avatar, text):
        '''Returns a achievement image in byte form.

        Returns a achievement image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        text (str): Text to be written on the image.
        '''

        return await self._get("/generators/achievement" if self.dev else "/achievement", "?avatar={}&text={}".format(avatar, text))

    async def thesearch(self, avatar, text):
        '''Returns a thesearch image in byte form.

        Returns a thesearch image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        text (str): Text to be written on the image.
        '''

        return await self._get("/generators/thesearch" if self.dev else "/thesearch", "?avatar={}&text={}".format(avatar, text))

    async def beautiful(self, avatar):
        '''Returns a beautiful image in byte form.

        Returns a beautiful image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        return await self._get("/generators/beautiful" if self.dev else "/beautiful", "?avatar={}".format(avatar))

    async def facepalm(self, avatar):
        '''Returns a facepalm image in byte form.

        Returns a facepalm image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        return await self._get("/generators/facepalm" if self.dev else "/facepalm", "?avatar={}".format(avatar))

    async def respect(self, avatar):
        '''Returns a respect image in byte form.

        Returns a respect image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        return await self._get("/generators/respect" if self.dev else "/respect", "?avatar={}".format(avatar))

    async def stepped(self, avatar):
        '''Returns a stepped image in byte form.

        Returns a stepped image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        return await self._get("/generators/stepped" if self.dev else "/stepped", "?avatar={}".format(avatar))

    async def tattoo(self, avatar):
        '''Returns a tattoo image in byte form.

        Returns a tattoo image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        return await self._get("/generators/tattoo" if self.dev else "/tattoo", "?avatar={}".format(avatar))

    async def vault(self, avatar):
        '''Returns a vault image in byte form.

        Returns a vault image in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        return await self._get("/generators/vault" if self.dev else "/vault", "?avatar={}".format(avatar))
       
    async def challenger(self, avatar):
        '''Returns a challenger image in byte form.

        Returns a challenger image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Challenger endpoint is disabled while in production")
        return await self._get("/generators/challenger", "?avatar={}".format(avatar))
       
    async def batslap(self, slapper, slapped):
        '''Returns a batslap image in byte form.

        Returns a batslap image in byte form. Write 
        it to an image file.

        Params:

        slapper (str): Link to the image of the slapper to be filtered.
        slapped (str): Link to the image of the slapped to be filtered.
        '''

        return await self._get("/generators/batslap" if self.dev else "/batslap", "?slapper={}&slapped={}".format(slapper, slapped))
       
    async def superpunch(self, puncher, punched):
        '''Returns a superpunch image in byte form.

        Returns a superpunch image in byte form. Write 
        it to an image file.

        Params:

        puncher (str): Link to the image of the puncher to be filtered.
        punched (str): Link to the image of the punched to be filtered.
        '''

        return await self._get("/generators/superpunch" if self.dev else "/superpunch", "?puncher={}&punched={}".format(puncher, punched))
       
    async def slap(self, slapper, slapped):
        '''Returns a slap image in byte form.

        Returns a slap image in byte form. Write 
        it to an image file.

        Params:

        slapper (str): Link to the image of the slapper to be filtered.
        slapped (str): Link to the image of the slapped to be filtered.
        '''

        return await self._get("/generators/slap" if self.dev else "/slap", "?slapper={}&slapped={}".format(slapper, slapped))
   
    async def karen(self, avatar):
        '''Returns a karen image in byte form.

        Returns a karen image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Karen endpoint is disabled while in production")
        return await self._get("/generators/karen", "?avatar={}".format(avatar))
       
    async def steam(self, avatar, text):
        '''Returns a steam image in byte form.

        Returns a steam image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        text (str): The text to be written on the image.
        '''

        if not self.dev:
            raise NotAvailable("Steam endpoint is disabled while in production")
        return await self._get("/generators/steam", "?avatar={}&text={}".format(avatar, text))

    async def bobross(self, avatar):
        '''Returns a bobross image in byte form.

        Returns a bobross image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Bobross endpoint is disabled while in production")
        return await self._get("/generators/bobross", "?avatar={}".format(avatar))

    async def heavyfear(self, avatar):
        '''Returns a heavyfear image in byte form.

        Returns a heavyfear image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Heavyfear endpoint is disabled while in production")
        return await self._get("/generators/heavyfear", "?avatar={}".format(avatar))

    async def painting(self, avatar):
        '''Returns a painting image in byte form.

        Returns a painting image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Painting endpoint is disabled while in production")
        return await self._get("/generators/painting", "?avatar={}".format(avatar))

    async def waifu_insult(self, avatar):
        '''Returns a waifu insult image in byte form.

        Returns a waifu insult image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Waifuinsult endpoint is disabled while in production")
        return await self._get("/generators/waifuinsult", "?avatar={}".format(avatar))

    async def wreckit(self, avatar):
        '''Returns a wreckit image in byte form.

        Returns a wreckit image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Wreckit endpoint is disabled while in production")
        return await self._get("/generators/wreckit", "?avatar={}".format(avatar))

    async def approved(self, avatar):
        '''Returns a approved image in byte form.

        Returns a approved image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Approved endpoint is disabled while in production")
        return await self._get("/overlays/approved", "?avatar={}".format(avatar))

    async def rainbow(self, avatar):
        '''Returns a rainbow image in byte form.

        Returns a rainbow image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Rainbow endpoint is disabled while in production")
        return await self._get("/overlays/rainbow", "?avatar={}".format(avatar))

    async def rejected(self, avatar):
        '''Returns a rejected image in byte form.

        Returns a rejected image in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Rejected endpoint is disabled while in production")
        return await self._get("/overlays/rejected", "?avatar={}".format(avatar))

    async def brightness(self, avatar, brightness):
        '''Returns a image with brightness in byte form.

        Returns a image with brightness in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        brightness (int): How much brightness to put on the image.
        '''

        if br_invalid(brightness):
            raise InvalidParam('Invalid brightness')
        if not self.dev:
            raise NotAvailable("Brightness endpoint is disabled while in production")
        return await self._get("/effects/brightness", "?avatar={}&brightness={}".format(avatar, brightness))

    async def darkness(self, avatar, darkness):
        '''Returns a image with darkness in byte form.

        Returns a image with darkness in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        darkness (int): How much darkness to put on the image.
        '''

        if br_invalid(darkness):
            raise InvalidParam('Invalid darkness')
        if not self.dev:
            raise NotAvailable("Darkness endpoint is disabled while in production")
        return await self._get("/effects/darkness", "?avatar={}&darkness={}".format(avatar, darkness))

    async def greyscale(self, avatar):
        '''Returns a image with greyscale in byte form.

        Returns a image with greyscale in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Greyscale endpoint is disabled while in production")
        return await self._get("/effects/greyscale", "?avatar={}".format(avatar))

    async def invert(self, avatar):
        '''Returns a image with invert in byte form.

        Returns a image with invert in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Invert endpoint is disabled while in production")
        return await self._get("/effects/invert", "?avatar={}".format(avatar))

    async def invert_greyscale(self, avatar):
        '''Returns a image with invertGreyscale in byte form.

        Returns a image with invertGreyscale in byte form. Write 
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("InvertGreyscale endpoint is disabled while in production")
        return await self._get("/effects/invertGreyscale", "?avatar={}".format(avatar))

    async def sepia(self, avatar):
        '''Returns a image with sepia in byte form.

        Returns a image with sepia in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Sepia endpoint is disabled while in production")
        return await self._get("/effects/sepia", "?avatar={}".format(avatar))

    async def silhouette(self, avatar):
        '''Returns a image with silhouette in byte form.

        Returns a image with silhouette in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        '''

        if not self.dev:
            raise NotAvailable("Silhouette endpoint is disabled while in production")
        return await self._get("/effects/silhouette", "?avatar={}".format(avatar))

    async def invert_threshold(self, avatar, threshold):
        '''Returns a image with inverted threshold in byte form.

        Returns a image with inverted threshold in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        threshold (int): How much threshold to put on the image.
        '''

        if br_invalid(threshold):
            raise InvalidParam('Invalid threshold')
        if not self.dev:
            raise NotAvailable("Threshold endpoint is disabled while in production")
        return await self._get("/effects/invertThreshold", "?avatar={}&threshold={}".format(avatar, threshold))

    async def threshold(self, avatar, threshold):
        '''Returns a image with threshold in byte form.

        Returns a image with threshold in byte form. Write
        it to an image file.

        Params:

        avatar (str): Link to the image to be filtered.
        threshold (int): How much threshold to put on the image.
        '''

        if br_invalid(threshold):
            raise InvalidParam('Invalid threshold')
        if not self.dev:
            raise NotAvailable("Threshold endpoint is disabled while in production")
        return await self._get("/effects/threshold", "?avatar={}&threshold={}".format(avatar, threshold))

    async def crush(self, crusher, crush):
        '''Returns a crush image in byte form.

        Returns a crush image in byte form. Write 
        it to an image file.

        Params:

        crusher (str): Link to the image of the crusher to be filtered.
        crush (str): Link to the image of the crush to be filtered.
        '''

        return await self._get("/generators/crush" if self.dev else "/crush", "?crusher={}&crush={}".format(crusher, crush))

    async def welcome(self, avatar, is_bot, usertag, guild, version="gearz"):
        '''Returns a welcome image in byte form.
        Deprecated see Client#greeting
        Returns a welcome image in byte form. Write
        it to an image file.

        Params:

        avatar (str): A link to the image to be filtered.
        isbot (bool): Whether the person is a bot or not.
        usertag (str): The user's tag.
        guild (str): The guild's name.
        version (str): Which Welcome picture to use.
        '''
        usertag_fixed = urllib.parse.quote(usertag)
        guild_fixed = urllib.parse.quote(guild)
        if not version == "gearz":
            if not self.dev:
                raise NotAvailable("Anime endpoint is disabled while in production")
            else:
                return await self._get("/greetings/{}_welcome".format(version), "?bot={}&usertag={}&avatar={}".format(is_bot, usertag, avatar))
        return await self._get("/greetings/{}_welcome".format(version) if self.dev else "/{}_welcome".format(version), "?guild={}&bot={}&usertag={}&avatar={}".format(guild_fixed, is_bot, usertag_fixed, avatar))

    async def goodbye(self, avatar, is_bot, usertag, version="gearz"):
        '''Returns a goodbye image in byte form.
        Deprecated see Client#greeting
        Returns a goodbye image in byte form. Write
        it to an image file.

        Params:

        avatar (str): A link to the image to be filtered.
        isbot (bool): Whether the person is a bot or not.
        usertag (str): The user's tag.
        version (str): Which Goodbye picture to use.
        '''
        usertag_fixed = urllib.parse.quote(usertag)
        if not self.dev:
            if not version == "gearz":
                raise NotAvailable("Anime endpoint is disabled while in production")
        return await self._get("/greetings/{}_goodbye".format(version) if self.dev else "/{}_goodbye".format(version), "?bot={}&usertag={}&avatar={}".format(is_bot, usertag_fixed, avatar))

    async def confused(self, avatar, photo):
        '''Returns a confused image in bytes.
        
        Params:
        avatar (str): Avatar url.
        photo (str): a url for second picture.
        '''
        if not self.dev: raise NotAvailable("Confused endpoint is disabled while in production")
        return await self._get("/generators/confused", "?avatar={}&photo={}".format(avatar, photo))

    async def garbage(self, avatar):
        '''Returns a garbage image in bytes.

        Params:

        avatar (str): Image url to use.
        '''
        if not self.dev: raise NotAvailable("Garbage endpoint is disabled while in production")
        return await self._get("/generators/garbage", "?avatar={}".format(avatar))

    async def super_spank(self, spanker, spanked):
        """Returns spanked image in bytes.
        Params:

        spanker (str): image url to use for spanker
        spanked (str): image url for spanked
        """
        if not self.dev: raise NotAvailable("Spanked endpoint is disabled while in production")
        return await self._get("/generators/superspank", "?spanker={}&spanked={}".format(spanker, spanked))
    async def tinder_match(self, avatar, match):
        """Returns a tinder match image in bytes
        Params:
        avatar (str): avatar image url
        match (str): image url for match image.
        """
        if not self.dev: raise NotAvailable("Tinder Match endpoint is disabled while in production")
        return await self._get("/generators/tinder", "?avatar={}&match={}".format(avatar, match))

    async def colour(self, colour):
        """Colour endpoint
        Params:
        colour (str): Supply a colour code in any of these supported formats `hex`, `rgb`, `rgba`
        """
        if not self.dev: raise NotAvailable("Colour endpoint is disabled while in production")
        return await self._get("/generators/colour", "?colour={}".format(colour))
    
    async def color(self, color):
        """Aliase for colour"""
        return await self.colour(color)
    
    async def owoify(self, text):
        """owoify a text.
        Params:
        text (str): The text you would like to use.
        """
        if not self.dev: raise NotAvailable("owoify endpoint is disabled while in production")
        if type(text) != str: raise TypeError("Text must be string")
        return await self._text("owoify", text)
    
    async def mock(self, text):
        """Mock a text
        Params:
        text (str): Text you would like to use
        """
        if not self.dev: raise NotAvailable("Mock endpoint is disabled while in production")
        if type(text) != str: raise TypeError("Text must be a string")
        return await self._text("mock", text)
    async def tiny(self, text, style):
        """Make a text tiny with a style.
        Params:
        text (str): Text to use.
        style (str): One of tiny, superscript, subscript
        """
        if not self.dev: raise NotAvailable("Tiny text endpoint is disabled while in production")
        if type(text) != str: raise TypeError("Text must be a string")
        if style.lower() not in ["tiny", "superscript", "subscript"]: raise TypeError("Style must be one of tiny, superscript, subscript")
        return await self._text("tinytext", text, style.lower())
 
    async def cursive(self, text, style):
        """Make a cursive text with specified style
        Params:
        text (str): Text you want to use.
        style (str): One of normal or bold
        """
        if not self.dev: raise NotAvailable("Cursive endpoint is disabled while in production")
        if type(text) != str: raise TypeError("Text must be a string")
        if style.lower() not in ["bold", "normal"]: raise TypeError("Style must be one of bold or normal")
        return await self._text("cursive", text, style.lower())

    async def vapor(self, text):
        """Returns a vaporwave text
        Params:
        text (str): Text you want to use.
        """
        if not self.dev: raise NotAvailable("Vapor endpoint is disabled while in production")
        if type(text) != str: raise TypeError("Text must be a string")
        return await self._text("vaporwave", text)
    
    async def time(self, avatar):
        """Returns a time image in bytes.
        Params:
        avatar (str): Avatar url to use.
        """
        if not self.dev: raise NotAvailable("Time endpoint is disabled while in production")
        return await self._get("/generators/time", "?avatar={}".format(avatar))
    
    async def ignore(self, avatar):
        """Returns an ignore image in bytes.
        Params:
        avatar (str): Avatar url to use.
        """
        if not self.dev: raise NotAvailable("Ignore endpoint is disabled while in production")
        return await self._get("/generators/ignore", "?avatar={}".format(avatar))
     
    async def hide(self, avatar):
        """Returns a hide image in bytes.
        Params:
        avatar (str): Avatar url to use.
        """
        if not self.dev: raise NotAvailable("Hide endpoint is disabled while in production")
        return await self._get("/generators/hide", "?avatar={}".format(avatar))
        
    async def hates(self, avatar):
        """Returns a time image in bytes.
        Params:
        avatar (str): Avatar url to use.
        """
        if not self.dev: raise NotAvailable("Hates endpoint is disabled while in production")
        return await self._get("/generators/hates", "?avatar={}".format(avatar))
        
    async def girls(self, avatar):
        """Returns girls image in bytes.
        Params:
        avatar (str): Avatar url to use.
        """
        if not self.dev: raise NotAvailable("Girls endpoint is disabled while in production")
        return await self._get("/generators/girls", "?avatar={}".format(avatar))
    
    async def zerotwo(self, avatar):
        """Returns a Zero Two image in bytes.
        Params:
        avatar (str): Avatar url to use.
        """
        if not self.dev: raise NotAvailable("Zero Two endpoint is disabled while in production")
        return await self._get("/generators/02picture", "?avatar={}".format(avatar))
    
    async def coffee(self, text1, text2):
        """Returns a coffee image in bytes.
        Params:
        text1 (str): Text 1 to use
        text2 (str): Text 2 to use
        """
        if not self.dev: raise NotAvailable("Coffee endpoint is disabled while in production")
        return await self._get("/generators/coffee", "?text1={}&text2={}".format(text1, text2))
    
    async def religion(self, avatar):
        """Returns a religion image in bytes.
        Params:
        avatar (str): Avatar url to use.
        """
        if not self.dev: raise NotAvailable("Religion endpoint is disabled while in production")
        return await self._get("/generators/religion", "?avatar={}".format(avatar))
        
    async def suggestion(self, avatar, text):
        """Returns a suggestion image in bytes.
        Params:
        avatar (str): Avatar url to use.
        text (str): Text to use.
        """
        if not self.dev: raise NotAvailable("Suggestion endpoint is disabled while in production")
        return await self._get("/generators/suggestion", "?avatar={}&suggestion={}".format(avatar, text))

    async def kirby(self, avatar, text):
        """Kirby School endpoint
        params:
        avatar (str): Image you expect to be used
        text (str): Supply the build up text
        returns (bytes) 
        """
        if not self.dev:
            raise NotAvailable("Kirby School endpoint is disabled while in production")
        return await self._get("/generators/kirby", "?avatar={}&text={}".format(avatar, text))

    async def virtual(self, avatar, text):
        """Virtual endpoint
        params:
        avatar (str): Image you expect to be used
        returns (bytes) 
        """
        if not self.dev:
            raise NotAvailable("Virtual endpoint is disabled while in production")
        return await self._get("/generators/vr", "?avatar={}".format(avatar))

    async def changemymind(self, avatar, text):
        """Change my mind endpoint
        params:
        avatar (str): Image you expect to be used
        text (str): Supply the build up text
        returns (bytes) 
        """
        if not self.dev:
            raise NotAvailable("Change my mind endpoint is disabled while in production")
        return await self._get("/generators/changemymind", "?avatar={}&text={}".format(avatar, text))
        
    async def sniper(self, avatar):
        """Sniper endpoint
        params:
        avatar (str): Image you expect to be used
        returns (bytes) 
        """
        if not self.dev:
            raise NotAvailable("Sniper endpoint is disabled while in production")
        return await self._get("/generators/sniper", "?avatar={}".format(avatar))

    async def osu(self, user, theme = "dark"):
        """osu! endpoint
        params:
        user (str): This is the osu! username.
        theme (str): Select between 3 valid themes, light, dark and darker
        returns (bytes) 
        """
        if not self.dev:
            raise NotAvailable("osu endpoint is disabled while in production")
        if theme not in ("dark", "light", "darker"):
            raise TypeError("Invalid theme, theme can only be one of dark, light, darker")
        return await self._get("/generators/osu", "?user={}&theme={}".format(user, theme))

    async def greeting(self, Type, version, bot, avatar, username, discriminator, guildName, memberCount, message = ""):
        """
        The new greetings endpoint
        params:
        Type: (str) Type of this greeting either welcome or farewell
        version: (str) The greetings version either gearz or anime
        bot: (bool) Wether the user is a bot
        avatar: (str) User's avatar url
        username: (str) Username
        discriminator: (str) User's last 4 digit discriminator
        guildName: (str) The server's name
        memberCount: (str) Current server's member count
        message: (str) = '' An optional message for the greeting
        returns: (bytes)
        """
        return await self._get("/greetings/unified", "?version={}&type={}&bot={}&avatar={}&username={}&discriminator={}&guildName={}&memberCount={}&message={}".format(version, Type, str(bot).lower(), avatar, username, discriminator, guildName, memberCount, message))




 


# --------------------
# |     Errors       |
# --------------------
class IdioticError(Exception):
    pass
class NotAvailable(IdioticError):
    pass
class InvalidParam(IdioticError):
    pass
# This file went longer than i expected :p
