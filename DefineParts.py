import itertools
import pickle

class devParts:
    """パーツ性能格納用クラス"""
    def __init__(self, name):
        self.name = name
        self.point = 0
        self.lv = 1
        self.power = 0
        self.aero = 0
        self.lightweight = 0
        self.handling = 0
        self.brake = 0

class performanceLank(devParts):
    """パフォーマンス値格納用クラス"""
    # 最高速
    def getTopSpeed(self):
        return self.power * 2 + self.aero // 2
    # 加速
    def getAccellarate(self):
        return self.aero + self.lightweight
    # コーナリング速度
    def getConaring(self):
        return self.handling * 2
    # ブレーキ性能
    def getBrakeRange(self):
        return self.brake * 2 + self.lightweight // 2

class calRandD:
    """研究開発計算クラス"""
    # パーツデータ
    datafile = '/mnt/d/python/100/temp/F1mobile/parts_all.csv'
    # パーツスロット数
    partsSlots = 8

    # コンストラクタ
    def __init__(self):
        self.datalist = []
        self.limitpoint = 0
        self.comb_max = 0

        with open(self.datafile, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('name'):
                    pass
                else:
                    items = line.split(',')
                    objParts = devParts(items[0])
                    objParts.point = int(items[1])
                    objParts.lv  = int(items[2])
                    objParts.power = int(items[3])
                    objParts.aero = int(items[4])
                    objParts.lightweight = int(items[5])
                    objParts.handling = int(items[6])
                    objParts.brake = int(items[7])
                    self.datalist.append(objParts)
    
    # データ一覧取得
    def getAllDatalist(self):
        return self.datalist
    
    # 名前を指定してパーツ名を取得
    # 存在しなかった場合はNoneを返す
    def getPartsByName(self):
        for i in self.datalist:
            if i.name == name:
                return i
        return None
    
    # 研究開発ポイント上限設定
    def setPointLimit(self, limit):
        self.limitpoint = limit
    
    # パーツの組み合わせ一覧を生成
    def generateCombination(self):
        # 研究開発ポイント上限が0(未設定)の場合はエラーとする
        if self.limitpoint == 0:
            raise NameError('set PointLimit before to generate combination!')

        # 全組み合わせを生成
        combi = itertools.combinations(self.datalist, self.partsSlots)
        print('combination generate...')

        # ポイント上限の判定と各値を合計
        out_combi = []
        for items in combi:
            # name は仮の値でオブジェクト生成
            parts_total = performanceLank('')
            for parts in items:
                parts_total.name += parts.name + ','
                parts_total.point += parts.point
                parts_total.power += parts.power
                parts_total.aero += parts.aero
                parts_total.lightweight += parts.lightweight
                parts_total.handling += parts.handling
                parts_total.brake += parts.brake
            # 研究開発ポイントが上限以上、または上限の70%未満の場合を除外
            if self.limitpoint >= parts_total.point and parts_total.point >= (self.limitpoint * 0.8):
                # name の末尾の,を取り除く
                parts_total.name = parts_total.name[:-1]
                #print(parts_total.name, parts_total.point)
                out_combi.append(parts_total)
                if (parts_total.getTopSpeed() + parts_total.getAccellarate() + parts_total.getConaring() + parts_total.getBrakeRange()) > self.comb_max:
                    self.comb_max = parts_total.getTopSpeed() + parts_total.getAccellarate() + parts_total.getConaring() + parts_total.getBrakeRange()
        
        # リストを返す
        return out_combi
