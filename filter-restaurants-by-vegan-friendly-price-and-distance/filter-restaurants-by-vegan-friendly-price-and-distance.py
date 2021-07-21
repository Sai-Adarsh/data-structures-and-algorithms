class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        
        
        res = []
        for id_val, rating_val, vegan_val, price_val, dist_val in restaurants:
            if veganFriendly:
                if vegan_val == 1:
                    if price_val <= maxPrice:
                        if dist_val <= maxDistance:
                            res.append((id_val, rating_val))
            else:
                if price_val <= maxPrice:
                    if dist_val <= maxDistance:
                        res.append((id_val, rating_val))
                        
                        
        res.sort(key = lambda x: (-x[1], -x[0]))
        return [i[0] for i in res]