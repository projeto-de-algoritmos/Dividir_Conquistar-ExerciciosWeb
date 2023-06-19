class Solution:
    def getSkyline(self, buildings):
        if not buildings:
            return []

        return self.mergeSkyline(buildings, 0, len(buildings) - 1)

    def mergeSkyline(self, buildings, left, right):
        if left == right:
            return [[buildings[left][0], buildings[left][2]], [buildings[left][1], 0]]

        mid = (left + right) // 2
        leftSkyline = self.mergeSkyline(buildings, left, mid)
        rightSkyline = self.mergeSkyline(buildings, mid + 1, right)

        return self.merge(leftSkyline, rightSkyline)

    def merge(self, leftSkyline, rightSkyline):
        mergedSkyline = []
        leftHeight, rightHeight = 0, 0
        i, j = 0, 0

        while i < len(leftSkyline) and j < len(rightSkyline):
            if leftSkyline[i][0] < rightSkyline[j][0]:
                x = leftSkyline[i][0]
                leftHeight = leftSkyline[i][1]
                maxH = max(leftHeight, rightHeight)
                if not mergedSkyline or maxH != mergedSkyline[-1][1]:
                    mergedSkyline.append([x, maxH])
                i += 1
            elif leftSkyline[i][0] > rightSkyline[j][0]:
                x = rightSkyline[j][0]
                rightHeight = rightSkyline[j][1]
                maxH = max(leftHeight, rightHeight)
                if not mergedSkyline or maxH != mergedSkyline[-1][1]:
                    mergedSkyline.append([x, maxH])
                j += 1
            else:
                x = leftSkyline[i][0]
                leftHeight = leftSkyline[i][1]
                rightHeight = rightSkyline[j][1]
                maxH = max(leftHeight, rightHeight)
                if not mergedSkyline or maxH != mergedSkyline[-1][1]:
                    mergedSkyline.append([x, maxH])
                i += 1
                j += 1

        while i < len(leftSkyline):
            mergedSkyline.append(leftSkyline[i])
            i += 1

        while j < len(rightSkyline):
            mergedSkyline.append(rightSkyline[j])
            j += 1

        return mergedSkyline
