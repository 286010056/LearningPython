import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_ig_msa():
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 输入
    ax.text(0.5, 9, 'Input Feature (X)', fontsize=10, ha='center')
    ax.text(0.5, 8.5, 'Illumination Feature (F_lu)', fontsize=10, ha='center')
    rect = patches.Rectangle((0, 8), 1, 1, linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(rect)

    # 线性投影
    ax.text(2, 9, 'Linear Q', fontsize=10, ha='center')
    ax.text(2, 8.5, 'Linear K', fontsize=10, ha='center')
    ax.text(2, 8, 'Linear V', fontsize=10, ha='center')
    ax.text(2, 7.5, 'Linear Y', fontsize=10, ha='center')
    rect = patches.Rectangle((1.5, 7), 1, 2.5, linewidth=1, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(rect)

    # 多头分割
    ax.text(4, 8.5, 'Split Heads', fontsize=10, ha='center')
    rect = patches.Rectangle((3.5, 8), 1, 1, linewidth=1, edgecolor='black', facecolor='yellow')
    ax.add_patch(rect)

    # 注意力计算
    ax.text(6, 8.5, 'Attention Head', fontsize=10, ha='center')
    rect = patches.Rectangle((5.5, 8), 1, 1, linewidth=1, edgecolor='black', facecolor='orange')
    ax.add_patch(rect)

    # 输出拼接
    ax.text(8, 8.5, 'Concat & Linear', fontsize=10, ha='center')
    rect = patches.Rectangle((7.5, 8), 1, 1, linewidth=1, edgecolor='black', facecolor='pink')
    ax.add_patch(rect)

    # 位置编码和残差
    ax.text(5, 6, 'Position Emb', fontsize=10, ha='center')
    rect = patches.Rectangle((4.5, 5.5), 1, 1, linewidth=1, edgecolor='black', facecolor='brown')
    ax.add_patch(rect)

    # 输出
    ax.text(9, 8.5, 'Output', fontsize=10, ha='center')
    rect = patches.Rectangle((8.5, 8), 1, 1, linewidth=1, edgecolor='black', facecolor='red')
    ax.add_patch(rect)

    # 连接线
    # 输入到线性投影
    ax.arrow(1, 8.5, 0.5, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
    # 线性投影到多头
    ax.arrow(2.5, 8.5, 1, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
    # 多头到注意力
    ax.arrow(4.5, 8.5, 1, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
    # 注意力到拼接
    ax.arrow(6.5, 8.5, 1, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
    # 拼接和位置编码到输出
    ax.arrow(8.5, 8.5, 0, -1, head_width=0.1, head_length=0.1, fc='k', ec='k')
    ax.arrow(5, 5.5, 3.5, 2, head_width=0.1, head_length=0.1, fc='k', ec='k')

    plt.show()

draw_ig_msa()