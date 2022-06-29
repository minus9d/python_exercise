"""
○○するスクリプト
"""
import argparse
import logging
from pathlib import Path
import sys
import time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-o', '--outdir', default='./outdir',
        help="出力ディレクトリ")

    args = parser.parse_args()
    return args


def setup_logger(logger_path: Path) -> logging.Logger:
    """loggerオブジェクトを生成

    Args:
        logger_path (Path): ログの書き込み先

    Returns:
        logger: loggerオブジェクト
    """

    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(logger_path)

    stream_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    handler_format = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    stream_handler.setFormatter(handler_format)
    file_handler.setFormatter(handler_format)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


def write_arguments(logger: logging.Logger, args: argparse.Namespace):
    """実行時引数をloggerに記録
    """
    logger.info(f"sys.argv:")
    logger.info(f"    {sys.argv}")
    logger.info(f"parsed args:")
    for key, value in vars(args).items():
        logger.info(f"    {key}: {value}")


def main():
    start_time = time.perf_counter()

    args = parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    logger_path = outdir / 'log.log'
    logger = setup_logger(logger_path)

    logger.info('start')
    write_arguments(logger, args)

    # ここに実処理を書く

    end_time = time.perf_counter()
    logger.info('finished ({:.2f} sec)'.format(end_time - start_time))


if __name__ == '__main__':
    main()
