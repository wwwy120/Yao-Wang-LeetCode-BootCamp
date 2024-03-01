class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """

        #Time Complexity: O(n^2)
        #Space Complexity: O(n)
        if time == 0:
            return 0
        else:
            new_clips = []
            maximum = 0
            new_time = time
            for i in range(len(clips)):
                if clips[i][1] < time:
                    new_clips += [clips[i]]
                else:
                    if time - clips[i][0] > maximum:
                        maximum = time - clips[i][0]
                        new_time = clips[i][0]
            if len(new_clips) == len(clips):
                return -1
            else:
                if self.videoStitching(new_clips, new_time) == -1:
                    return -1
                else:
                    return 1 + self.videoStitching(new_clips, new_time)
