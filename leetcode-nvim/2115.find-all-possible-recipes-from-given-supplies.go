package main

// @leet start
func findAllRecipes(recipes []string, ingredients [][]string, supplies []string) []string {
	suppliesMap := make(map[string]bool)
	for _, s := range supplies {
		suppliesMap[s] = true
	}
	recipes2Ingre := make(map[string][]string)
	for i, r := range recipes {
		recipes2Ingre[r] = ingredients[i]
	}

	cache := make(map[string]bool)
	var canProduce func(recipe string) bool
	canProduce = func(recipe string) bool {
		// in cache
		if res, inCache := cache[recipe]; inCache {
			return res
		}
		ans := true
		for _, ingre := range recipes2Ingre[recipe] {
			if _, canSupply := suppliesMap[ingre]; canSupply {
				continue
			}
			if _, inRecipes := recipes2Ingre[ingre]; inRecipes {
				// backtrack technique to avoid infinite cycle
				temp := recipes2Ingre[recipe]
				delete(recipes2Ingre, recipe)
				res := canProduce(ingre)
				recipes2Ingre[recipe] = temp
				if res {
					continue
				}
			}
			ans = false
			break
		}
		cache[recipe] = ans
		return ans
	}

	ans := []string{}
	for _, r := range recipes {
		if canProduce(r) {
			ans = append(ans, r)
		}
	}
	return ans
}

// @leet end

