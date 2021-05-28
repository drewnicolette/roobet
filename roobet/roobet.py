import hashlib
import hmac

salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"

class Crash():
    def __init__(self) -> None:
        pass

    def hmac_hash(self,hash_code: str):
        """ Gets HMAC HASH

        Args:
            hash_code (str): [description]

        Returns:
            [type]: [description]
        """
        return hmac.new(hash_code.encode(), salt.encode(),
                        digestmod=hashlib.sha256).hexdigest()


    def get_multiplier(self,hash_code: str):
        """ Returns multiplier of crash game

        Args:
            hash_code (str): 

        Returns:
            type: Float
        """
        hash_hex = self.hmac_hash(hash_code)
        if (int(hash_hex, 16) % 20 == 0):
            return 1
        h = int(hash_hex[:13], 16)
        e = 2 ** 52
        return (((100 * e - h) / (e - h)) // 1) / 100.0

    def get_prev_game(self,hash_code: str):
        """Returns Previous Games Hash Code

        Args:
            hash_code (string): Hash of Game

        Returns:
            type: String
        """
        m = hashlib.sha256()
        m.update(hash_code.encode("utf-8"))
        return m.hexdigest()

    def get_number_games_since_hash(self, hash_code: str):
        """ Returns number of games since inputted hashcode

        Args:
            hash_code (str): Hash of Game
        Returns:
            type: Integer
        """
        first_game = "77b271fe12fca03c618f63dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"
        count = 0
        game_hash = hash_code
        while game_hash != first_game:
            count += 1
            game_hash = self.get_prev_game(game_hash)
        
        return count