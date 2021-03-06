# coding: utf-8
# created by liu hui
import chess
import datetime

# 全局变量，用于存储已经走过的着法，最多存储8步
pre_moves = []

max_time = 2.6

abs_max_weight = 666666


# 存储权重的数组 white
weights_white = [100, 100, 100, 100, 100, 100, 100, 100,
                 105, 110, 110, 80, 80, 110, 110, 105,
                 105, 95, 90, 100, 100, 90, 95, 105,
                 100, 100, 100, 120, 120, 100, 100, 100,
                 105, 105, 110, 125, 125, 110, 105, 105,
                 110, 110, 120, 130, 130, 120, 110, 110,
                 150, 150, 150, 150, 150, 150, 150, 150,
                 100, 100, 100, 100, 100, 100, 100, 100,

                 250, 260, 270, 270, 270, 270, 260, 250,
                 260, 280, 300, 305, 305, 300, 280, 260,
                 270, 305, 310, 305, 305, 310, 305, 270,
                 270, 300, 315, 320, 320, 315, 300, 270,
                 270, 305, 315, 320, 320, 315, 305, 270,
                 270, 300, 310, 315, 315, 310, 300, 270,
                 260, 280, 300, 300, 300, 300, 280, 260,
                 250, 260, 270, 270, 270, 270, 250, 250,

                 280, 290, 290, 290, 290, 290, 290, 280,
                 290, 305, 300, 300, 300, 300, 305, 290,
                 290, 310, 310, 310, 310, 310, 310, 290,
                 290, 300, 310, 310, 310, 310, 300, 290,
                 290, 305, 305, 310, 310, 305, 305, 290,
                 290, 300, 305, 310, 310, 305, 300, 290,
                 290, 300, 300, 300, 300, 300, 300, 290,
                 280, 290, 290, 290, 290, 290, 290, 280,

                 500, 500, 500, 505, 505, 500, 500, 500,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 505, 510, 510, 510, 510, 510, 510, 505,
                 500, 500, 500, 500, 500, 500, 500, 500,

                 880, 890, 890, 895, 895, 890, 890, 880,
                 890, 900, 905, 900, 900, 900, 900, 890,
                 890, 905, 905, 905, 905, 905, 900, 890,
                 900, 900, 905, 905, 905, 905, 900, 895,
                 895, 900, 905, 905, 905, 905, 900, 895,
                 890, 900, 905, 905, 905, 905, 900, 890,
                 890, 900, 900, 900, 900, 900, 900, 890,
                 880, 890, 890, 895, 895, 890, 890, 880,

                 9020, 9030, 9010, 9000, 9000, 9010, 9030, 9020,
                 9020, 9020, 9000, 9000, 9000, 9000, 9020, 9020,
                 8990, 8980, 8980, 8980, 8980, 8980, 8980, 8990,
                 8980, 8970, 8970, 8960, 8960, 8970, 8970, 8980,
                 8970, 8960, 8960, 8950, 8950, 8960, 8960, 8970,
                 8970, 8960, 8960, 8950, 8950, 8960, 8960, 8970,
                 8970, 8960, 8960, 8950, 8950, 8960, 8960, 8970,
                 8970, 8960, 8960, 8950, 8950, 8960, 8960, 8970]

# 存储权重的数组 black
weights_black = [100, 100, 100, 100, 100, 100, 100, 100,
                 150, 150, 150, 150, 150, 150, 150, 150,
                 110, 110, 120, 130, 130, 120, 110, 110,
                 105, 105, 110, 125, 125, 110, 105, 105,
                 100, 100, 100, 120, 120, 100, 100, 100,
                 105, 95, 90, 100, 100, 90, 95, 105,
                 105, 110, 110, 100, 100, 110, 110, 105,
                 100, 100, 100, 100, 100, 100, 100, 100,

                 250, 260, 270, 270, 270, 270, 260, 250,
                 260, 280, 300, 305, 305, 300, 280, 260,
                 270, 305, 310, 315, 315, 310, 305, 270,
                 270, 300, 315, 320, 320, 315, 300, 270,
                 270, 300, 315, 320, 320, 315, 300, 270,
                 270, 305, 310, 315, 315, 310, 305, 270,
                 260, 280, 300, 300, 300, 300, 280, 260,
                 250, 260, 270, 270, 270, 270, 260, 250,

                 280, 290, 290, 290, 290, 290, 290, 280,
                 290, 300, 300, 300, 300, 300, 300, 290,
                 290, 300, 305, 310, 310, 305, 300, 290,
                 290, 305, 305, 310, 310, 305, 305, 290,
                 290, 300, 310, 310, 310, 310, 300, 290,
                 290, 310, 310, 310, 310, 310, 310, 290,
                 290, 305, 300, 300, 300, 300, 305, 290,
                 280, 290, 290, 290, 290, 290, 290, 280,

                 500, 500, 500, 500, 500, 500, 500, 500,
                 505, 510, 510, 510, 510, 510, 510, 505,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 495, 500, 500, 500, 500, 500, 500, 495,
                 500, 500, 500, 505, 505, 500, 500, 500,

                 880, 890, 890, 895, 895, 890, 890, 880,
                 890, 900, 905, 900, 900, 900, 900, 890,
                 890, 905, 905, 905, 905, 905, 900, 890,
                 900, 900, 905, 905, 905, 905, 900, 895,
                 895, 900, 905, 905, 905, 905, 900, 895,
                 890, 900, 905, 905, 905, 905, 900, 890,
                 890, 900, 900, 900, 900, 900, 900, 890,
                 880, 890, 890, 895, 895, 890, 890, 880,

                 8970, 8960, 8960, 8950, 8950, 8960, 8960, 8970,
                 8970, 8960, 8960, 8950, 8950, 8960, 8960, 8970,
                 8970, 8960, 8960, 8950, 8950, 8960, 8960, 8970,
                 8970, 8960, 8960, 8950, 8950, 8960, 8960, 8970,
                 8980, 8970, 8970, 8960, 8960, 8970, 8970, 8980,
                 8990, 8980, 8980, 8980, 8980, 8980, 8980, 8990,
                 9020, 9020, 9000, 9000, 9000, 9000, 9020, 9020,
                 9020, 9030, 9010, 9000, 9000, 9010, 9030, 9020]

index_list = [0, 1, 2, 3, 4, 5, 6, 7,
              8, 9, 10, 11, 12, 13, 14, 15,
              16, 17, 18, 19, 20, 21, 22, 23,
              24, 25, 26, 27, 28, 29, 30, 31,
              32, 33, 34, 35, 36, 37, 38, 39,
              40, 41, 42, 43, 44, 45, 46, 47,
              48, 49, 50, 51, 52, 53, 54, 55,
              56, 57, 58, 59, 60, 61, 62, 63]


# chess ai 接口
def ai_alpha_beta(fen, is_white, depth, alpha, beta, start, sorted_moves):
    board = chess.Board(fen)

    if len(sorted_moves) > 0:
        legal_moves = list(reversed(sorted_moves))
    else:
        legal_moves = list(board.legal_moves)

    # 最好的着法best_mov，较好的着法moves_queue
    best_mov = legal_moves[0]
    moves_queue = [best_mov]
    sorted_moves = []

    # 如果是白色方下棋，则选择权重最小的一种走法
    if is_white:
        for mov in legal_moves:
            board.push(mov)
            cal_weight = ai_alpha_beta_au(board.fen(), not is_white, depth - 1, alpha, beta, start)
            board.pop()
            if cal_weight < beta:
                beta = cal_weight
                moves_queue.append(mov)
                sorted_moves.append(mov)
            else:
                sorted_moves.insert(0, mov)
            if (datetime.datetime.now() - start).total_seconds() >= max_time:
                return best_mov, sorted_moves, beta
        cal_weight = beta

    # 如果是黑色方，则选择权重最大的一种走法
    else:
        for mov in legal_moves:
            board.push(mov)
            cal_weight = ai_alpha_beta_au(board.fen(), not is_white, depth - 1, alpha, beta, start)
            board.pop()
            if cal_weight > alpha:
                alpha = cal_weight
                moves_queue.append(mov)
                sorted_moves.append(mov)
            else:
                sorted_moves.insert(0, mov)
                # beta解肢
            if (datetime.datetime.now() - start).total_seconds() >= max_time:
                return best_mov, sorted_moves, alpha
        cal_weight = alpha

    # 防止出现重复5步的逻辑
    best_mov = moves_queue.pop()
    if len(pre_moves) < 8:
        pre_moves.append(best_mov)
    else:
        if best_mov == pre_moves[0] and best_mov == pre_moves[2] \
                and best_mov == pre_moves[4] and best_mov == pre_moves[6] \
                and len(moves_queue) > 0:
            best_mov = moves_queue.pop()
        pre_moves.pop(0)
        pre_moves.append(best_mov)
    return best_mov, sorted_moves, cal_weight


def ai_alpha_beta_au(fen, is_white, depth, alpha, beta, start):
    board = chess.Board(fen)

    # depth大于0
    if depth > 0:

        # 如果是白色方下棋，则选择权重最小的一种走法
        if is_white:
            for mov in board.legal_moves:
                board.push(mov)
                cal_weight = ai_alpha_beta_au(board.fen(), not is_white, depth-1, alpha, beta, start)
                board.pop()
                if cal_weight < beta:
                    beta = cal_weight
                    # alpha解肢
                    if beta <= alpha:
                        break
                if (datetime.datetime.now() - start).total_seconds() >= max_time:
                    break
            return beta

        # 如果是黑色方，则选择权重最大的一种走法
        else:
            for mov in list(board.legal_moves):
                board.push(mov)
                cal_weight = ai_alpha_beta_au(board.fen(), not is_white, depth-1, alpha, beta, start)
                board.pop()
                if cal_weight > alpha:
                    alpha = cal_weight
                    # beta解肢
                    if beta <= alpha:
                        break
                if (datetime.datetime.now() - start).total_seconds() >= max_time:
                    break
            return alpha

    # depth为0 计算weight
    elif not board.is_game_over():
        weight = 0
        for i in index_list:
            pos = board.piece_at(i)
            if pos is None:
                continue
            index = (pos.piece_type-1) * 64 + i
            if pos.color is True:
                weight -= weights_white[index]
            else:
                weight += weights_black[index]
        return weight

    # 游戏结束
    else:
        if is_white:
            return abs_max_weight
        else:
            return -abs_max_weight


def respond_to(fen):
    is_white = chess.Board(fen).turn

    mov = {}
    cal_mov = {}
    # 第一层搜索的深度为2
    depth = 2
    start = datetime.datetime.now()
    cost = 0

    # 存储第一层着法排完序之后的序列
    sorted_moves = []
    weight = 0

    while cost < max_time:
        # 只有在规定时间3s内一层完全计算完，才更新相应的uci
        # 如果一层没有计算完全便更新相应的uci则会有bug，ai便会很傻
        mov = cal_mov
        if depth <= 4:
            cal_mov, sorted_moves, weight = \
                ai_alpha_beta(fen, is_white, depth, -abs_max_weight, abs_max_weight, start, sorted_moves)
        else:
            cal_mov, sorted_moves, weight = \
                ai_alpha_beta(fen, is_white, depth, weight - 25, weight + 25, start, sorted_moves)
        cost = (datetime.datetime.now() - start).total_seconds()
        print cost
        if cost < max_time:
            print "total compute depth %d" % depth
        depth += 1

    return mov.uci()
