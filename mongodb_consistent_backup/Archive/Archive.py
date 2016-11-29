import logging

from Tar import Tar


class Archive:
    def __init__(self, config, backup_dir):
        self.config     = config
        self.backup_dir = backup_dir

        self._archiver = None
        self.init()

    def init(self):
        if self.config.archive.method == "tar":
            logging.info("Using archiving method: tar (compression: %s)" % self.config.archive.compression)
            try:
                self._archiver = Tar(
                    self.config,
                    self.backup_dir
                )
            except Exception, e:
                raise e
        else:
            logging.info("Archiving disabled, skipping")

    def archive(self):
        if self._archiver:
            return self._archiver.run()

    def close(self):
        if self._archiver:
            return self._archiver.close()
