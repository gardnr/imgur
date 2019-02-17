from imgurpython import ImgurClient

from gardnr import constants, drivers


class Imgur(drivers.Exporter):

    whitelist = [constants.Metrics.IMAGE]

    def export(self, logs):
        client = ImgurClient(
            self.client_id,
            self.client_secret,
            refresh_token=self.refresh_token
        )

        image_ids = []
        for log in logs:
            image = client.upload_from_path(
                log.value,
                config={'description': log.timestamp.isoformat()},
                anon=False
            )

            image_ids.append(image['id'])

        client.album_add_images(self.album_id, image_ids)
