from trezor.messages.LiskPublicKey import LiskPublicKey

from .helpers import LISK_CURVE

from apps.common import layout, seed


async def get_public_key(ctx, msg):
    node = await seed.derive_node(ctx, msg.address_n, LISK_CURVE)
    pubkey = node.public_key()
    pubkey = pubkey[1:]  # skip ed25519 pubkey marker

    if msg.show_display:
        await layout.show_pubkey(ctx, pubkey)

    return LiskPublicKey(public_key=pubkey)
