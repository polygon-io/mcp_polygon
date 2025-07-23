import os
import json
from typing import Optional, Any, Dict, Union, List, Literal
from mcp.server.fastmcp import FastMCP
from polygon import RESTClient
from importlib.metadata import version, PackageNotFoundError

from datetime import datetime, date

POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY", "")
if not POLYGON_API_KEY:
    print("Warning: POLYGON_API_KEY environment variable not set.")

version_number = "MCP-Polygon/unknown"
try:
    version_number = f"MCP-Polygon/{version('mcp_polygon')}"
except PackageNotFoundError:
    pass

polygon_client = RESTClient(POLYGON_API_KEY)
polygon_client.headers["User-Agent"] += f" {version_number}"

poly_mcp = FastMCP("Polygon", dependencies=["polygon"])


@poly_mcp.tool()
async def get_aggs(
    ticker: str,
    multiplier: int,
    timespan: str,
    from_: Union[str, int, datetime, date],
    to: Union[str, int, datetime, date],
    adjusted: Optional[bool] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List aggregate bars for a ticker over a given date range in custom time window sizes.
    """
    try:
        results = polygon_client.get_aggs(
            ticker=ticker,
            multiplier=multiplier,
            timespan=timespan,
            from_=from_,
            to=to,
            adjusted=adjusted,
            sort=sort,
            limit=limit,
            params=params,
            raw=True,
        )

        # Parse the binary data to string and then to JSON
        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_aggs(
    ticker: str,
    multiplier: int,
    timespan: str,
    from_: Union[str, int, datetime, date],
    to: Union[str, int, datetime, date],
    adjusted: Optional[bool] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Iterate through aggregate bars for a ticker over a given date range.
    """
    try:
        results = polygon_client.list_aggs(
            ticker=ticker,
            multiplier=multiplier,
            timespan=timespan,
            from_=from_,
            to=to,
            adjusted=adjusted,
            sort=sort,
            limit=limit,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_grouped_daily_aggs(
    date: str,
    adjusted: Optional[bool] = None,
    include_otc: Optional[bool] = None,
    locale: Optional[str] = None,
    market_type: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get grouped daily bars for entire market for a specific date.
    """
    try:
        results = polygon_client.get_grouped_daily_aggs(
            date=date,
            adjusted=adjusted,
            include_otc=include_otc,
            locale=locale,
            market_type=market_type,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_daily_open_close_agg(
    ticker: str,
    date: str,
    adjusted: Optional[bool] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get daily open, close, high, and low for a specific ticker and date.
    """
    try:
        results = polygon_client.get_daily_open_close_agg(
            ticker=ticker, date=date, adjusted=adjusted, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_previous_close_agg(
    ticker: str,
    adjusted: Optional[bool] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get previous day's open, close, high, and low for a specific ticker.
    """
    try:
        results = polygon_client.get_previous_close_agg(
            ticker=ticker, adjusted=adjusted, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_trades(
    ticker: str,
    timestamp: Optional[Union[str, int, datetime, date]] = None,
    timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
    timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
    timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
    timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get trades for a ticker symbol.
    """
    try:
        results = polygon_client.list_trades(
            ticker=ticker,
            timestamp=timestamp,
            timestamp_lt=timestamp_lt,
            timestamp_lte=timestamp_lte,
            timestamp_gt=timestamp_gt,
            timestamp_gte=timestamp_gte,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_last_trade(
    ticker: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get the most recent trade for a ticker symbol.
    """
    try:
        results = polygon_client.get_last_trade(ticker=ticker, params=params, raw=True)

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_last_crypto_trade(
    from_: str,
    to: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get the most recent trade for a crypto pair.
    """
    try:
        results = polygon_client.get_last_crypto_trade(
            from_=from_, to=to, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_quotes(
    ticker: str,
    timestamp: Optional[Union[str, int, datetime, date]] = None,
    timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
    timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
    timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
    timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get quotes for a ticker symbol.
    """
    try:
        results = polygon_client.list_quotes(
            ticker=ticker,
            timestamp=timestamp,
            timestamp_lt=timestamp_lt,
            timestamp_lte=timestamp_lte,
            timestamp_gt=timestamp_gt,
            timestamp_gte=timestamp_gte,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_last_quote(
    ticker: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get the most recent quote for a ticker symbol.
    """
    try:
        results = polygon_client.get_last_quote(ticker=ticker, params=params, raw=True)

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_last_forex_quote(
    from_: str,
    to: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get the most recent forex quote.
    """
    try:
        results = polygon_client.get_last_forex_quote(
            from_=from_, to=to, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_real_time_currency_conversion(
    from_: str,
    to: str,
    amount: Optional[float] = None,
    precision: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get real-time currency conversion.
    """
    try:
        results = polygon_client.get_real_time_currency_conversion(
            from_=from_,
            to=to,
            amount=amount,
            precision=precision,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_universal_snapshots(
    type: str,
    ticker_any_of: Optional[List[str]] = None,
    order: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get universal snapshots for multiple assets of a specific type.
    """
    try:
        results = polygon_client.list_universal_snapshots(
            type=type,
            ticker_any_of=ticker_any_of,
            order=order,
            limit=limit,
            sort=sort,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_snapshot_all(
    market_type: str,
    tickers: Optional[List[str]] = None,
    include_otc: Optional[bool] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get a snapshot of all tickers in a market.
    """
    try:
        results = polygon_client.get_snapshot_all(
            market_type=market_type,
            tickers=tickers,
            include_otc=include_otc,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_snapshot_direction(
    market_type: str,
    direction: str,
    include_otc: Optional[bool] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get gainers or losers for a market.
    """
    try:
        results = polygon_client.get_snapshot_direction(
            market_type=market_type,
            direction=direction,
            include_otc=include_otc,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_snapshot_ticker(
    market_type: str,
    ticker: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get snapshot for a specific ticker.
    """
    try:
        results = polygon_client.get_snapshot_ticker(
            market_type=market_type, ticker=ticker, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_snapshot_option(
    underlying_asset: str,
    option_contract: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get snapshot for a specific option contract.
    """
    try:
        results = polygon_client.get_snapshot_option(
            underlying_asset=underlying_asset,
            option_contract=option_contract,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_snapshot_crypto_book(
    ticker: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get snapshot for a crypto ticker's order book.
    """
    try:
        results = polygon_client.get_snapshot_crypto_book(
            ticker=ticker, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_market_holidays(
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get upcoming market holidays and their open/close times.
    """
    try:
        results = polygon_client.get_market_holidays(params=params, raw=True)

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_market_status(
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get current trading status of exchanges and financial markets.
    """
    try:
        results = polygon_client.get_market_status(params=params, raw=True)

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_tickers(
    ticker: Optional[str] = None,
    type: Optional[str] = None,
    market: Optional[str] = None,
    exchange: Optional[str] = None,
    cusip: Optional[str] = None,
    cik: Optional[str] = None,
    date: Optional[Union[str, datetime, date]] = None,
    search: Optional[str] = None,
    active: Optional[bool] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    limit: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Query supported ticker symbols across stocks, indices, forex, and crypto.
    """
    try:
        results = polygon_client.list_tickers(
            ticker=ticker,
            type=type,
            market=market,
            exchange=exchange,
            cusip=cusip,
            cik=cik,
            date=date,
            search=search,
            active=active,
            sort=sort,
            order=order,
            limit=limit,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_ticker_details(
    ticker: str,
    date: Optional[Union[str, datetime, date]] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get detailed information about a specific ticker.
    """
    try:
        results = polygon_client.get_ticker_details(
            ticker=ticker, date=date, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_ticker_news(
    ticker: Optional[str] = None,
    published_utc: Optional[Union[str, datetime, date]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get recent news articles for a stock ticker.
    """
    try:
        results = polygon_client.list_ticker_news(
            ticker=ticker,
            published_utc=published_utc,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_ticker_types(
    asset_class: Optional[str] = None,
    locale: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List all ticker types supported by Polygon.io.
    """
    try:
        results = polygon_client.get_ticker_types(
            asset_class=asset_class, locale=locale, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_splits(
    ticker: Optional[str] = None,
    execution_date: Optional[Union[str, datetime, date]] = None,
    reverse_split: Optional[bool] = None,
    limit: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get historical stock splits.
    """
    try:
        results = polygon_client.list_splits(
            ticker=ticker,
            execution_date=execution_date,
            reverse_split=reverse_split,
            limit=limit,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_dividends(
    ticker: Optional[str] = None,
    ex_dividend_date: Optional[Union[str, datetime, date]] = None,
    frequency: Optional[int] = None,
    dividend_type: Optional[str] = None,
    limit: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get historical cash dividends.
    """
    try:
        results = polygon_client.list_dividends(
            ticker=ticker,
            ex_dividend_date=ex_dividend_date,
            frequency=frequency,
            dividend_type=dividend_type,
            limit=limit,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_conditions(
    asset_class: Optional[str] = None,
    data_type: Optional[str] = None,
    id: Optional[int] = None,
    sip: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List conditions used by Polygon.io.
    """
    try:
        results = polygon_client.list_conditions(
            asset_class=asset_class,
            data_type=data_type,
            id=id,
            sip=sip,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_exchanges(
    asset_class: Optional[str] = None,
    locale: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List exchanges known by Polygon.io.
    """
    try:
        results = polygon_client.get_exchanges(
            asset_class=asset_class, locale=locale, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_stock_financials(
    ticker: Optional[str] = None,
    cik: Optional[str] = None,
    company_name: Optional[str] = None,
    company_name_search: Optional[str] = None,
    sic: Optional[str] = None,
    filing_date: Optional[Union[str, datetime, date]] = None,
    filing_date_lt: Optional[Union[str, datetime, date]] = None,
    filing_date_lte: Optional[Union[str, datetime, date]] = None,
    filing_date_gt: Optional[Union[str, datetime, date]] = None,
    filing_date_gte: Optional[Union[str, datetime, date]] = None,
    period_of_report_date: Optional[Union[str, datetime, date]] = None,
    period_of_report_date_lt: Optional[Union[str, datetime, date]] = None,
    period_of_report_date_lte: Optional[Union[str, datetime, date]] = None,
    period_of_report_date_gt: Optional[Union[str, datetime, date]] = None,
    period_of_report_date_gte: Optional[Union[str, datetime, date]] = None,
    timeframe: Optional[str] = None,
    include_sources: Optional[bool] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get fundamental financial data for companies.
    """
    try:
        results = polygon_client.vx.list_stock_financials(
            ticker=ticker,
            cik=cik,
            company_name=company_name,
            company_name_search=company_name_search,
            sic=sic,
            filing_date=filing_date,
            filing_date_lt=filing_date_lt,
            filing_date_lte=filing_date_lte,
            filing_date_gt=filing_date_gt,
            filing_date_gte=filing_date_gte,
            period_of_report_date=period_of_report_date,
            period_of_report_date_lt=period_of_report_date_lt,
            period_of_report_date_lte=period_of_report_date_lte,
            period_of_report_date_gt=period_of_report_date_gt,
            period_of_report_date_gte=period_of_report_date_gte,
            timeframe=timeframe,
            include_sources=include_sources,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_ipos(
    ticker: Optional[str] = None,
    listing_date: Optional[Union[str, datetime, date]] = None,
    listing_date_lt: Optional[Union[str, datetime, date]] = None,
    listing_date_lte: Optional[Union[str, datetime, date]] = None,
    listing_date_gt: Optional[Union[str, datetime, date]] = None,
    listing_date_gte: Optional[Union[str, datetime, date]] = None,
    ipo_status: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Retrieve upcoming or historical IPOs.
    """
    try:
        results = polygon_client.vx.list_ipos(
            ticker=ticker,
            listing_date=listing_date,
            listing_date_lt=listing_date_lt,
            listing_date_lte=listing_date_lte,
            listing_date_gt=listing_date_gt,
            listing_date_gte=listing_date_gte,
            ipo_status=ipo_status,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_short_interest(
    ticker: Optional[str] = None,
    settlement_date: Optional[Union[str, datetime, date]] = None,
    settlement_date_lt: Optional[Union[str, datetime, date]] = None,
    settlement_date_lte: Optional[Union[str, datetime, date]] = None,
    settlement_date_gt: Optional[Union[str, datetime, date]] = None,
    settlement_date_gte: Optional[Union[str, datetime, date]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Retrieve short interest data for stocks.
    """
    try:
        results = polygon_client.vx.list_short_interest(
            ticker=ticker,
            settlement_date=settlement_date,
            settlement_date_lt=settlement_date_lt,
            settlement_date_lte=settlement_date_lte,
            settlement_date_gt=settlement_date_gt,
            settlement_date_gte=settlement_date_gte,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_short_volume(
    ticker: Optional[str] = None,
    date: Optional[Union[str, datetime, date]] = None,
    date_lt: Optional[Union[str, datetime, date]] = None,
    date_lte: Optional[Union[str, datetime, date]] = None,
    date_gt: Optional[Union[str, datetime, date]] = None,
    date_gte: Optional[Union[str, datetime, date]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Retrieve short volume data for stocks.
    """
    try:
        results = polygon_client.vx.list_short_volume(
            ticker=ticker,
            date=date,
            date_lt=date_lt,
            date_lte=date_lte,
            date_gt=date_gt,
            date_gte=date_gte,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_treasury_yields(
    date: Optional[Union[str, datetime, date]] = None,
    date_lt: Optional[Union[str, datetime, date]] = None,
    date_lte: Optional[Union[str, datetime, date]] = None,
    date_gt: Optional[Union[str, datetime, date]] = None,
    date_gte: Optional[Union[str, datetime, date]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Retrieve treasury yield data.
    """
    try:
        results = polygon_client.vx.list_treasury_yields(
            date=date,
            date_lt=date_lt,
            date_lte=date_lte,
            date_gt=date_gt,
            date_gte=date_gte,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_benzinga_analyst_insights(
    date: Optional[Union[str, date]] = None,
    date_any_of: Optional[str] = None,
    date_gt: Optional[Union[str, date]] = None,
    date_gte: Optional[Union[str, date]] = None,
    date_lt: Optional[Union[str, date]] = None,
    date_lte: Optional[Union[str, date]] = None,
    ticker: Optional[str] = None,
    ticker_any_of: Optional[str] = None,
    ticker_gt: Optional[str] = None,
    ticker_gte: Optional[str] = None,
    ticker_lt: Optional[str] = None,
    ticker_lte: Optional[str] = None,
    last_updated: Optional[str] = None,
    last_updated_any_of: Optional[str] = None,
    last_updated_gt: Optional[str] = None,
    last_updated_gte: Optional[str] = None,
    last_updated_lt: Optional[str] = None,
    last_updated_lte: Optional[str] = None,
    firm: Optional[str] = None,
    firm_any_of: Optional[str] = None,
    firm_gt: Optional[str] = None,
    firm_gte: Optional[str] = None,
    firm_lt: Optional[str] = None,
    firm_lte: Optional[str] = None,
    rating_action: Optional[str] = None,
    rating_action_any_of: Optional[str] = None,
    rating_action_gt: Optional[str] = None,
    rating_action_gte: Optional[str] = None,
    rating_action_lt: Optional[str] = None,
    rating_action_lte: Optional[str] = None,
    benzinga_firm_id: Optional[str] = None,
    benzinga_firm_id_any_of: Optional[str] = None,
    benzinga_firm_id_gt: Optional[str] = None,
    benzinga_firm_id_gte: Optional[str] = None,
    benzinga_firm_id_lt: Optional[str] = None,
    benzinga_firm_id_lte: Optional[str] = None,
    benzinga_rating_id: Optional[str] = None,
    benzinga_rating_id_any_of: Optional[str] = None,
    benzinga_rating_id_gt: Optional[str] = None,
    benzinga_rating_id_gte: Optional[str] = None,
    benzinga_rating_id_lt: Optional[str] = None,
    benzinga_rating_id_lte: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List Benzinga analyst insights.
    """
    try:
        results = polygon_client.list_benzinga_analyst_insights(
            date=date,
            date_any_of=date_any_of,
            date_gt=date_gt,
            date_gte=date_gte,
            date_lt=date_lt,
            date_lte=date_lte,
            ticker=ticker,
            ticker_any_of=ticker_any_of,
            ticker_gt=ticker_gt,
            ticker_gte=ticker_gte,
            ticker_lt=ticker_lt,
            ticker_lte=ticker_lte,
            last_updated=last_updated,
            last_updated_any_of=last_updated_any_of,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            firm=firm,
            firm_any_of=firm_any_of,
            firm_gt=firm_gt,
            firm_gte=firm_gte,
            firm_lt=firm_lt,
            firm_lte=firm_lte,
            rating_action=rating_action,
            rating_action_any_of=rating_action_any_of,
            rating_action_gt=rating_action_gt,
            rating_action_gte=rating_action_gte,
            rating_action_lt=rating_action_lt,
            rating_action_lte=rating_action_lte,
            benzinga_firm_id=benzinga_firm_id,
            benzinga_firm_id_any_of=benzinga_firm_id_any_of,
            benzinga_firm_id_gt=benzinga_firm_id_gt,
            benzinga_firm_id_gte=benzinga_firm_id_gte,
            benzinga_firm_id_lt=benzinga_firm_id_lt,
            benzinga_firm_id_lte=benzinga_firm_id_lte,
            benzinga_rating_id=benzinga_rating_id,
            benzinga_rating_id_any_of=benzinga_rating_id_any_of,
            benzinga_rating_id_gt=benzinga_rating_id_gt,
            benzinga_rating_id_gte=benzinga_rating_id_gte,
            benzinga_rating_id_lt=benzinga_rating_id_lt,
            benzinga_rating_id_lte=benzinga_rating_id_lte,
            limit=limit,
            sort=sort,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_benzinga_analysts(
    benzinga_id: Optional[str] = None,
    benzinga_id_any_of: Optional[str] = None,
    benzinga_id_gt: Optional[str] = None,
    benzinga_id_gte: Optional[str] = None,
    benzinga_id_lt: Optional[str] = None,
    benzinga_id_lte: Optional[str] = None,
    benzinga_firm_id: Optional[str] = None,
    benzinga_firm_id_any_of: Optional[str] = None,
    benzinga_firm_id_gt: Optional[str] = None,
    benzinga_firm_id_gte: Optional[str] = None,
    benzinga_firm_id_lt: Optional[str] = None,
    benzinga_firm_id_lte: Optional[str] = None,
    firm_name: Optional[str] = None,
    firm_name_any_of: Optional[str] = None,
    firm_name_gt: Optional[str] = None,
    firm_name_gte: Optional[str] = None,
    firm_name_lt: Optional[str] = None,
    firm_name_lte: Optional[str] = None,
    full_name: Optional[str] = None,
    full_name_any_of: Optional[str] = None,
    full_name_gt: Optional[str] = None,
    full_name_gte: Optional[str] = None,
    full_name_lt: Optional[str] = None,
    full_name_lte: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List Benzinga analysts.
    """
    try:
        results = polygon_client.list_benzinga_analysts(
            benzinga_id=benzinga_id,
            benzinga_id_any_of=benzinga_id_any_of,
            benzinga_id_gt=benzinga_id_gt,
            benzinga_id_gte=benzinga_id_gte,
            benzinga_id_lt=benzinga_id_lt,
            benzinga_id_lte=benzinga_id_lte,
            benzinga_firm_id=benzinga_firm_id,
            benzinga_firm_id_any_of=benzinga_firm_id_any_of,
            benzinga_firm_id_gt=benzinga_firm_id_gt,
            benzinga_firm_id_gte=benzinga_firm_id_gte,
            benzinga_firm_id_lt=benzinga_firm_id_lt,
            benzinga_firm_id_lte=benzinga_firm_id_lte,
            firm_name=firm_name,
            firm_name_any_of=firm_name_any_of,
            firm_name_gt=firm_name_gt,
            firm_name_gte=firm_name_gte,
            firm_name_lt=firm_name_lt,
            firm_name_lte=firm_name_lte,
            full_name=full_name,
            full_name_any_of=full_name_any_of,
            full_name_gt=full_name_gt,
            full_name_gte=full_name_gte,
            full_name_lt=full_name_lt,
            full_name_lte=full_name_lte,
            limit=limit,
            sort=sort,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_benzinga_consensus_ratings(
    ticker: str,
    date: Optional[Union[str, date]] = None,
    date_gt: Optional[Union[str, date]] = None,
    date_gte: Optional[Union[str, date]] = None,
    date_lt: Optional[Union[str, date]] = None,
    date_lte: Optional[Union[str, date]] = None,
    limit: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List Benzinga consensus ratings for a ticker.
    """
    try:
        results = polygon_client.list_benzinga_consensus_ratings(
            ticker=ticker,
            date=date,
            date_gt=date_gt,
            date_gte=date_gte,
            date_lt=date_lt,
            date_lte=date_lte,
            limit=limit,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_benzinga_earnings(
    date: Optional[Union[str, date]] = None,
    date_any_of: Optional[str] = None,
    date_gt: Optional[Union[str, date]] = None,
    date_gte: Optional[Union[str, date]] = None,
    date_lt: Optional[Union[str, date]] = None,
    date_lte: Optional[Union[str, date]] = None,
    ticker: Optional[str] = None,
    ticker_any_of: Optional[str] = None,
    ticker_gt: Optional[str] = None,
    ticker_gte: Optional[str] = None,
    ticker_lt: Optional[str] = None,
    ticker_lte: Optional[str] = None,
    importance: Optional[int] = None,
    importance_any_of: Optional[str] = None,
    importance_gt: Optional[int] = None,
    importance_gte: Optional[int] = None,
    importance_lt: Optional[int] = None,
    importance_lte: Optional[int] = None,
    last_updated: Optional[str] = None,
    last_updated_any_of: Optional[str] = None,
    last_updated_gt: Optional[str] = None,
    last_updated_gte: Optional[str] = None,
    last_updated_lt: Optional[str] = None,
    last_updated_lte: Optional[str] = None,
    date_status: Optional[str] = None,
    date_status_any_of: Optional[str] = None,
    date_status_gt: Optional[str] = None,
    date_status_gte: Optional[str] = None,
    date_status_lt: Optional[str] = None,
    date_status_lte: Optional[str] = None,
    eps_surprise_percent: Optional[float] = None,
    eps_surprise_percent_any_of: Optional[str] = None,
    eps_surprise_percent_gt: Optional[float] = None,
    eps_surprise_percent_gte: Optional[float] = None,
    eps_surprise_percent_lt: Optional[float] = None,
    eps_surprise_percent_lte: Optional[float] = None,
    revenue_surprise_percent: Optional[float] = None,
    revenue_surprise_percent_any_of: Optional[str] = None,
    revenue_surprise_percent_gt: Optional[float] = None,
    revenue_surprise_percent_gte: Optional[float] = None,
    revenue_surprise_percent_lt: Optional[float] = None,
    revenue_surprise_percent_lte: Optional[float] = None,
    fiscal_year: Optional[int] = None,
    fiscal_year_any_of: Optional[str] = None,
    fiscal_year_gt: Optional[int] = None,
    fiscal_year_gte: Optional[int] = None,
    fiscal_year_lt: Optional[int] = None,
    fiscal_year_lte: Optional[int] = None,
    fiscal_period: Optional[str] = None,
    fiscal_period_any_of: Optional[str] = None,
    fiscal_period_gt: Optional[str] = None,
    fiscal_period_gte: Optional[str] = None,
    fiscal_period_lt: Optional[str] = None,
    fiscal_period_lte: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List Benzinga earnings.
    """
    try:
        results = polygon_client.list_benzinga_earnings(
            date=date,
            date_any_of=date_any_of,
            date_gt=date_gt,
            date_gte=date_gte,
            date_lt=date_lt,
            date_lte=date_lte,
            ticker=ticker,
            ticker_any_of=ticker_any_of,
            ticker_gt=ticker_gt,
            ticker_gte=ticker_gte,
            ticker_lt=ticker_lt,
            ticker_lte=ticker_lte,
            importance=importance,
            importance_any_of=importance_any_of,
            importance_gt=importance_gt,
            importance_gte=importance_gte,
            importance_lt=importance_lt,
            importance_lte=importance_lte,
            last_updated=last_updated,
            last_updated_any_of=last_updated_any_of,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            date_status=date_status,
            date_status_any_of=date_status_any_of,
            date_status_gt=date_status_gt,
            date_status_gte=date_status_gte,
            date_status_lt=date_status_lt,
            date_status_lte=date_status_lte,
            eps_surprise_percent=eps_surprise_percent,
            eps_surprise_percent_any_of=eps_surprise_percent_any_of,
            eps_surprise_percent_gt=eps_surprise_percent_gt,
            eps_surprise_percent_gte=eps_surprise_percent_gte,
            eps_surprise_percent_lt=eps_surprise_percent_lt,
            eps_surprise_percent_lte=eps_surprise_percent_lte,
            revenue_surprise_percent=revenue_surprise_percent,
            revenue_surprise_percent_any_of=revenue_surprise_percent_any_of,
            revenue_surprise_percent_gt=revenue_surprise_percent_gt,
            revenue_surprise_percent_gte=revenue_surprise_percent_gte,
            revenue_surprise_percent_lt=revenue_surprise_percent_lt,
            revenue_surprise_percent_lte=revenue_surprise_percent_lte,
            fiscal_year=fiscal_year,
            fiscal_year_any_of=fiscal_year_any_of,
            fiscal_year_gt=fiscal_year_gt,
            fiscal_year_gte=fiscal_year_gte,
            fiscal_year_lt=fiscal_year_lt,
            fiscal_year_lte=fiscal_year_lte,
            fiscal_period=fiscal_period,
            fiscal_period_any_of=fiscal_period_any_of,
            fiscal_period_gt=fiscal_period_gt,
            fiscal_period_gte=fiscal_period_gte,
            fiscal_period_lt=fiscal_period_lt,
            fiscal_period_lte=fiscal_period_lte,
            limit=limit,
            sort=sort,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_benzinga_firms(
    benzinga_id: Optional[str] = None,
    benzinga_id_any_of: Optional[str] = None,
    benzinga_id_gt: Optional[str] = None,
    benzinga_id_gte: Optional[str] = None,
    benzinga_id_lt: Optional[str] = None,
    benzinga_id_lte: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List Benzinga firms.
    """
    try:
        results = polygon_client.list_benzinga_firms(
            benzinga_id=benzinga_id,
            benzinga_id_any_of=benzinga_id_any_of,
            benzinga_id_gt=benzinga_id_gt,
            benzinga_id_gte=benzinga_id_gte,
            benzinga_id_lt=benzinga_id_lt,
            benzinga_id_lte=benzinga_id_lte,
            limit=limit,
            sort=sort,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_benzinga_guidance(
    date: Optional[Union[str, date]] = None,
    date_any_of: Optional[str] = None,
    date_gt: Optional[Union[str, date]] = None,
    date_gte: Optional[Union[str, date]] = None,
    date_lt: Optional[Union[str, date]] = None,
    date_lte: Optional[Union[str, date]] = None,
    ticker: Optional[str] = None,
    ticker_any_of: Optional[str] = None,
    ticker_gt: Optional[str] = None,
    ticker_gte: Optional[str] = None,
    ticker_lt: Optional[str] = None,
    ticker_lte: Optional[str] = None,
    positioning: Optional[str] = None,
    positioning_any_of: Optional[str] = None,
    positioning_gt: Optional[str] = None,
    positioning_gte: Optional[str] = None,
    positioning_lt: Optional[str] = None,
    positioning_lte: Optional[str] = None,
    importance: Optional[int] = None,
    importance_any_of: Optional[str] = None,
    importance_gt: Optional[int] = None,
    importance_gte: Optional[int] = None,
    importance_lt: Optional[int] = None,
    importance_lte: Optional[int] = None,
    last_updated: Optional[str] = None,
    last_updated_any_of: Optional[str] = None,
    last_updated_gt: Optional[str] = None,
    last_updated_gte: Optional[str] = None,
    last_updated_lt: Optional[str] = None,
    last_updated_lte: Optional[str] = None,
    fiscal_year: Optional[int] = None,
    fiscal_year_any_of: Optional[str] = None,
    fiscal_year_gt: Optional[int] = None,
    fiscal_year_gte: Optional[int] = None,
    fiscal_year_lt: Optional[int] = None,
    fiscal_year_lte: Optional[int] = None,
    fiscal_period: Optional[str] = None,
    fiscal_period_any_of: Optional[str] = None,
    fiscal_period_gt: Optional[str] = None,
    fiscal_period_gte: Optional[str] = None,
    fiscal_period_lt: Optional[str] = None,
    fiscal_period_lte: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List Benzinga guidance.
    """
    try:
        results = polygon_client.list_benzinga_guidance(
            date=date,
            date_any_of=date_any_of,
            date_gt=date_gt,
            date_gte=date_gte,
            date_lt=date_lt,
            date_lte=date_lte,
            ticker=ticker,
            ticker_any_of=ticker_any_of,
            ticker_gt=ticker_gt,
            ticker_gte=ticker_gte,
            ticker_lt=ticker_lt,
            ticker_lte=ticker_lte,
            positioning=positioning,
            positioning_any_of=positioning_any_of,
            positioning_gt=positioning_gt,
            positioning_gte=positioning_gte,
            positioning_lt=positioning_lt,
            positioning_lte=positioning_lte,
            importance=importance,
            importance_any_of=importance_any_of,
            importance_gt=importance_gt,
            importance_gte=importance_gte,
            importance_lt=importance_lt,
            importance_lte=importance_lte,
            last_updated=last_updated,
            last_updated_any_of=last_updated_any_of,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            fiscal_year=fiscal_year,
            fiscal_year_any_of=fiscal_year_any_of,
            fiscal_year_gt=fiscal_year_gt,
            fiscal_year_gte=fiscal_year_gte,
            fiscal_year_lt=fiscal_year_lt,
            fiscal_year_lte=fiscal_year_lte,
            fiscal_period=fiscal_period,
            fiscal_period_any_of=fiscal_period_any_of,
            fiscal_period_gt=fiscal_period_gt,
            fiscal_period_gte=fiscal_period_gte,
            fiscal_period_lt=fiscal_period_lt,
            fiscal_period_lte=fiscal_period_lte,
            limit=limit,
            sort=sort,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_benzinga_news(
    published: Optional[str] = None,
    published_any_of: Optional[str] = None,
    published_gt: Optional[str] = None,
    published_gte: Optional[str] = None,
    published_lt: Optional[str] = None,
    published_lte: Optional[str] = None,
    last_updated: Optional[str] = None,
    last_updated_any_of: Optional[str] = None,
    last_updated_gt: Optional[str] = None,
    last_updated_gte: Optional[str] = None,
    last_updated_lt: Optional[str] = None,
    last_updated_lte: Optional[str] = None,
    tickers: Optional[str] = None,
    tickers_all_of: Optional[str] = None,
    tickers_any_of: Optional[str] = None,
    channels: Optional[str] = None,
    channels_all_of: Optional[str] = None,
    channels_any_of: Optional[str] = None,
    tags: Optional[str] = None,
    tags_all_of: Optional[str] = None,
    tags_any_of: Optional[str] = None,
    author: Optional[str] = None,
    author_any_of: Optional[str] = None,
    author_gt: Optional[str] = None,
    author_gte: Optional[str] = None,
    author_lt: Optional[str] = None,
    author_lte: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List Benzinga news.
    """
    try:
        results = polygon_client.list_benzinga_news(
            published=published,
            published_any_of=published_any_of,
            published_gt=published_gt,
            published_gte=published_gte,
            published_lt=published_lt,
            published_lte=published_lte,
            last_updated=last_updated,
            last_updated_any_of=last_updated_any_of,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            tickers=tickers,
            tickers_all_of=tickers_all_of,
            tickers_any_of=tickers_any_of,
            channels=channels,
            channels_all_of=channels_all_of,
            channels_any_of=channels_any_of,
            tags=tags,
            tags_all_of=tags_all_of,
            tags_any_of=tags_any_of,
            author=author,
            author_any_of=author_any_of,
            author_gt=author_gt,
            author_gte=author_gte,
            author_lt=author_lt,
            author_lte=author_lte,
            limit=limit,
            sort=sort,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_benzinga_ratings(
    date: Optional[Union[str, date]] = None,
    date_any_of: Optional[str] = None,
    date_gt: Optional[Union[str, date]] = None,
    date_gte: Optional[Union[str, date]] = None,
    date_lt: Optional[Union[str, date]] = None,
    date_lte: Optional[Union[str, date]] = None,
    ticker: Optional[str] = None,
    ticker_any_of: Optional[str] = None,
    ticker_gt: Optional[str] = None,
    ticker_gte: Optional[str] = None,
    ticker_lt: Optional[str] = None,
    ticker_lte: Optional[str] = None,
    importance: Optional[int] = None,
    importance_any_of: Optional[str] = None,
    importance_gt: Optional[int] = None,
    importance_gte: Optional[int] = None,
    importance_lt: Optional[int] = None,
    importance_lte: Optional[int] = None,
    last_updated: Optional[str] = None,
    last_updated_any_of: Optional[str] = None,
    last_updated_gt: Optional[str] = None,
    last_updated_gte: Optional[str] = None,
    last_updated_lt: Optional[str] = None,
    last_updated_lte: Optional[str] = None,
    rating_action: Optional[str] = None,
    rating_action_any_of: Optional[str] = None,
    rating_action_gt: Optional[str] = None,
    rating_action_gte: Optional[str] = None,
    rating_action_lt: Optional[str] = None,
    rating_action_lte: Optional[str] = None,
    price_target_action: Optional[str] = None,
    price_target_action_any_of: Optional[str] = None,
    price_target_action_gt: Optional[str] = None,
    price_target_action_gte: Optional[str] = None,
    price_target_action_lt: Optional[str] = None,
    price_target_action_lte: Optional[str] = None,
    benzinga_id: Optional[str] = None,
    benzinga_id_any_of: Optional[str] = None,
    benzinga_id_gt: Optional[str] = None,
    benzinga_id_gte: Optional[str] = None,
    benzinga_id_lt: Optional[str] = None,
    benzinga_id_lte: Optional[str] = None,
    benzinga_analyst_id: Optional[str] = None,
    benzinga_analyst_id_any_of: Optional[str] = None,
    benzinga_analyst_id_gt: Optional[str] = None,
    benzinga_analyst_id_gte: Optional[str] = None,
    benzinga_analyst_id_lt: Optional[str] = None,
    benzinga_analyst_id_lte: Optional[str] = None,
    benzinga_firm_id: Optional[str] = None,
    benzinga_firm_id_any_of: Optional[str] = None,
    benzinga_firm_id_gt: Optional[str] = None,
    benzinga_firm_id_gte: Optional[str] = None,
    benzinga_firm_id_lt: Optional[str] = None,
    benzinga_firm_id_lte: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    List Benzinga ratings.
    """
    try:
        results = polygon_client.list_benzinga_ratings(
            date=date,
            date_any_of=date_any_of,
            date_gt=date_gt,
            date_gte=date_gte,
            date_lt=date_lt,
            date_lte=date_lte,
            ticker=ticker,
            ticker_any_of=ticker_any_of,
            ticker_gt=ticker_gt,
            ticker_gte=ticker_gte,
            ticker_lt=ticker_lt,
            ticker_lte=ticker_lte,
            importance=importance,
            importance_any_of=importance_any_of,
            importance_gt=importance_gt,
            importance_gte=importance_gte,
            importance_lt=importance_lt,
            importance_lte=importance_lte,
            last_updated=last_updated,
            last_updated_any_of=last_updated_any_of,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            rating_action=rating_action,
            rating_action_any_of=rating_action_any_of,
            rating_action_gt=rating_action_gt,
            rating_action_gte=rating_action_gte,
            rating_action_lt=rating_action_lt,
            rating_action_lte=rating_action_lte,
            price_target_action=price_target_action,
            price_target_action_any_of=price_target_action_any_of,
            price_target_action_gt=price_target_action_gt,
            price_target_action_gte=price_target_action_gte,
            price_target_action_lt=price_target_action_lt,
            price_target_action_lte=price_target_action_lte,
            benzinga_id=benzinga_id,
            benzinga_id_any_of=benzinga_id_any_of,
            benzinga_id_gt=benzinga_id_gt,
            benzinga_id_gte=benzinga_id_gte,
            benzinga_id_lt=benzinga_id_lt,
            benzinga_id_lte=benzinga_id_lte,
            benzinga_analyst_id=benzinga_analyst_id,
            benzinga_analyst_id_any_of=benzinga_analyst_id_any_of,
            benzinga_analyst_id_gt=benzinga_analyst_id_gt,
            benzinga_analyst_id_gte=benzinga_analyst_id_gte,
            benzinga_analyst_id_lt=benzinga_analyst_id_lt,
            benzinga_analyst_id_lte=benzinga_analyst_id_lte,
            benzinga_firm_id=benzinga_firm_id,
            benzinga_firm_id_any_of=benzinga_firm_id_any_of,
            benzinga_firm_id_gt=benzinga_firm_id_gt,
            benzinga_firm_id_gte=benzinga_firm_id_gte,
            benzinga_firm_id_lt=benzinga_firm_id_lt,
            benzinga_firm_id_lte=benzinga_firm_id_lte,
            limit=limit,
            sort=sort,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


# Directly expose the MCP server object
# It will be run from entrypoint.py


def run(transport: Literal["stdio", "sse", "streamable-http"] = "stdio") -> None:
    """Run the Polygon MCP server."""
    poly_mcp.run(transport)
