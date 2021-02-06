import pickle

import DefineParts

## メイン処理
x = DefineParts.calRandD()
x.setPointLimit(58)

out = x.generateCombination()

f = open('generate.pb','wb')
pickle.dump(out,f)
f.close

# 誤差率
# 目標となる誤差率の初期値を50にセット
#total_error_rate = 50
# 最高速、加速、コーナリング、ブレーキの性能比率を配列で指定
#target_rate = [1, 1, 1, 1]

#for i in out:
#    target_total_rate = target_rate[0] + target_rate[1] + target_rate[2] + target_rate[3]
#    comb_total = i.getTopSpeed() + i.getAccellarate() + i.getConaring() + i.getBrakeRange()
#    target_perform_TopSp = abs((i.getTopSpeed() / ((comb_total / target_total_rate) * target_rate[0]) * 100) - 100 )
#    target_perform_Accel = abs((i.getAccellarate() / ((comb_total / target_total_rate) * target_rate[1]) * 100) - 100 )
#    target_perform_Cornar = abs((i.getConaring() / ((comb_total / target_total_rate) * target_rate[2]) * 100) - 100 )
#    target_perform_Brake = abs((i.getBrakeRange() / ((comb_total / target_total_rate) * target_rate[3]) * 100) - 100 )
#    target_error_rate = max(target_perform_TopSp, target_perform_Accel, target_perform_Cornar, target_perform_Brake)
    # 誤差率をパフォーマンス値の最大値に対する比率で補正(パフォーマンス値が大きい方が優位とする)
#    target_error_rate = target_error_rate * (x.comb_max / comb_total)

#    if total_error_rate > target_error_rate:
#        total_error_rate = target_error_rate
#        print(i.name, i.point, i.getTopSpeed(), i.getAccellarate(), i.getConaring(), i.getBrakeRange(), " /最大誤差率", int(total_error_rate), "%")

