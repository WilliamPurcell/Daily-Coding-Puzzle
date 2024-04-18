class Solution(object):
    def maxArea(self, height):

        left=0
        right = len(height)-1
        maxwater= abs(left-right)* min(height[left],height[right])
        while left<right:
            if height[left]<height[right]:
                left +=1
            else :
                right-=1
            width=abs(left-right)
            wallheight=min(height[left],height[right])
            if maxwater<width*wallheight:
                maxwater= width*wallheight
        return maxwater

        