'''
cat_dog - Return True if the string "cat" and "dog" appear the same number of times in the given string.

Expected Output:
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

'''
def cat_dog(str):
    dog_cnt = 0
    cat_cnt = 0

    for i in range(0, len(str) - 2, 1):
        if str[i:i+3] == "cat":
            cat_cnt += 1
        if str[i:i+3] == "dog":
            dog_cnt += 1

        return dog_cnt == cat_cnt

'''
  #Approach 2: This is a standard count instance and compare results technique
  #
  # 012345678 
  # cataaadog length = 9
  # XXX   XXX
  #
  # [0:3] [6:9]
  # Length of reading frame? The reading frame is three.

'''