import hashlib
import hmac

salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"
first_game = "77b271fe12fca03c618f63dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"

class Crash():
    def __init__(self) -> None:
        pass

    def hmac_hash(self,hash_code: str):
        """ Gets HMAC HASH

        Args:
            hash_code (str): [description]

        Returns:
            string : HMAC Hash
        """
        return hmac.new(hash_code.encode(), salt.encode(),
                        digestmod=hashlib.sha256).hexdigest()


    def get_multiplier(self,hash_code: str):
        """ Returns multiplier of crash game

        Args:
            hash_code (str): 

        Returns:
            float : Multiplier of Hash Code
        """
        try:
            hash_hex = self.hmac_hash(hash_code)
            if (int(hash_hex, 16) % 20 == 0):
                return 1
            h = int(hash_hex[:13], 16)
            e = 2 ** 52
            return (((100 * e - h) / (e - h)) // 1) / 100.0
        except:
            print("Error getting Hash Multiplier")

    def get_prev_game(self,hash_code: str):
        """Returns Previous Games Hash Code

        Args:
            hash_code (string): Hash of Game

        Returns:
            m.hexdigest (str) : Previous Hash Code
        """
        try:
            m = hashlib.sha256()
            m.update(hash_code.encode("utf-8"))
            return m.hexdigest()
        except:
            print("Error getting Previous Game Hash")

    def get_number_games_since_hash(self, hash_code: str):
        """ Returns number of games since inputted hashcode

        Args:
            hash_code (str): Hash of Game
        Returns:
            count (integer) : The number of games since inputted hash_code
        """
        count = 0
        game_hash = hash_code
        try:
            while game_hash != first_game:
                count += 1
                game_hash = self.get_prev_game(game_hash)
            
            return count
        except:
            print("Error getting number of games")

    def get_highest_crash_amount(self, hash_code: str):
        """Gets the hash crash amount since hash code inputted

        Args:
            hash_code (str): Hash of Game

        Returns:
            highest_amount (float) : Highest Crash Amount since inputted hash_code
        """
        highest_amount = 0
        game_hash = hash_code
        try:
            while game_hash != first_game:
                if self.get_multiplier(game_hash) > highest_amount:
                    highest_amount = self.get_multiplier(game_hash)
                game_hash = self.get_prev_game(game_hash)
            return highest_amount
        except:
            print("Error returning highest crash amount")

    def get_times_crashed_at_one_in_row(self, hash_code: str):
        """Returns the number of times crash has crashed at 1.00x in a row

        Args:
            hash_code (str): Hash of Game

        Returns:
            highest (int) : Count of times in a row
        """
        highest = 0
        count = 0
        game_hash = hash_code
        try:
            while game_hash != first_game:
                if self.get_multiplier(game_hash) == 1.00:
                    count += 1
                    if count > highest:
                        highest = count
                else:
                    count = 0
                game_hash = self.get_prev_game(game_hash)
            return highest
        except:
            print("Error returning highest crash amount")

    def get_times_crashed_below(self, hash_code: str, multiplier: float):
        """Returns the number of times crash has crashed below specified multiplier in a row

        Args:
            hash_code (str): Hash of Game
            amount_under (float): Multiplier Crashed

        Returns:
            highest (int) : Count of times in a row
        """
        highest = 0
        count = 0
        game_hash = hash_code
        if multiplier < 1:
            raise("Amount Can Not be Under One... Please try again...")
        try:
            while game_hash != first_game:
                if self.get_multiplier(game_hash) < multiplier:
                    count += 1
                    if count > highest:
                        highest = count
                else:
                    count = 0
                game_hash = self.get_prev_game(game_hash)
            return highest
        except:
            print("Error returning amount under times in a row")

    def get_times_crashed_above(self, hash_code: str, multiplier: float):
        """Returns the number of times crash has crashed above specified multiplier in a row

        Args:
            hash_code (str): Hash of Game
            amount_under (float): Multiplier Crashed

        Returns:
            highest (int) : Count of times in a row
        """
        highest = 0
        count = 0
        game_hash = hash_code
        if multiplier < 1:
            raise("Amount Can Not be Under One... Please try again...")
        try:
            while game_hash != first_game:
                if self.get_multiplier(game_hash) > multiplier:
                    count += 1
                    if count > highest:
                        highest = count
                else:
                    count = 0
                game_hash = self.get_prev_game(game_hash)
            return highest
        except:
            print("Error returning amount under times in a row")


