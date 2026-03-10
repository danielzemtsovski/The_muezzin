from logger import Logger

logger = Logger.get_logger()

class Calculation:
    def __init__(self, hostile_list, very_hostile_list):
        self.hostile_list = hostile_list
        self.very_hostile_list = very_hostile_list

    def analyze_message(self, text):
        hostile_count = 0 
        very_hostile_count = 0
        words = text.lower().split()
        sum_words = len(words)

        for word in words:
            if word in self.hostile_list:
                hostile_count += 1
            elif word in self.very_hostile_list:
                very_hostile_count += 1

        total_hostile = hostile_count * 1 + very_hostile_count * 2
        bds_percent = (total_hostile / sum_words) * 100

        is_bds = bds_percent > 10
        if bds_percent > 20:
            bds_threat_level = "high"
        elif bds_percent > 10:
            bds_threat_level = "medium"
        else:
            bds_threat_level = "none"
        logger.info(f"Analyzed message: total_hostile={total_hostile}, percent={bds_percent:.2f}%, level={bds_threat_level}")
        return bds_percent, is_bds, bds_threat_level